# Importa los módulos necesarios
import random  # Para generar números aleatorios
import sys     # Para interactuar con el sistema, como salir del juego

# --- Definiciones de Clases ---

# Define la clase para los objetos del juego
class Item:
    # El constructor se llama al crear un nuevo objeto
    def __init__(self, name, description, item_type="misc", damage=0):
        self.name = name                # Nombre del objeto
        self.description = description  # Descripción del objeto
        self.item_type = item_type      # Tipo de objeto (ej. "weapon", "key")
        self.damage = damage            # Daño que hace el objeto si es un arma

# Define la clase para las criaturas del juego
class Creature:
    # Constructor para inicializar una criatura
    def __init__(self, name, description, health, attack_power):
        self.name = name                # Nombre de la criatura
        self.description = description  # Descripción de la criatura
        self.health = health            # Puntos de vida de la criatura
        self.attack_power = attack_power  # Poder de ataque de la criatura

    # Método para que la criatura hable
    def talk(self):
        return f"{self.name} gruñe amenazadoramente."

    # Método para que la criatura ataque a un objetivo
    def attack(self, target):
        # Calcula un daño aleatorio dentro de un rango
        damage = random.randint(self.attack_power // 2, self.attack_power)
        print(f"{self.name} ataca a {target.name} por {damage} de daño!")
        target.health -= damage  # Reduce la vida del objetivo
        # Asegura que la vida no sea negativa
        if target.health < 0:
            target.health = 0

# Define la clase para el jefe final, que hereda de Creature
class Boss(Creature):
    # Constructor que llama al constructor de la clase padre
    def __init__(self, name, description, health, attack_power):
        super().__init__(name, description, health, attack_power)
    
    # Método de hablar específico para el jefe
    def talk(self):
        return f"{self.name} ruge: '¡No pasarás!'"

# Define la clase para el jugador
class Player:
    # Constructor para inicializar al jugador
    def __init__(self, name, current_room):
        self.name = name                  # Nombre del jugador
        self.inventory = []               # Inventario inicial vacío
        self.current_room = current_room  # Habitación actual del jugador
        self.health = 100                 # Salud inicial del jugador
        self.base_attack_power = 5        # Poder de ataque base

    # Propiedad que devuelve el arma equipada del jugador
    @property
    def weapon(self):
        # Recorre el inventario en busca de un arma
        for item in self.inventory:
            if item.item_type == "weapon":
                return item
        return None  # Devuelve None si no hay arma
        
    # Propiedad que calcula el poder de ataque total del jugador
    @property
    def attack_power(self):
        power = self.base_attack_power
        # Si tiene un arma, suma su daño
        if self.weapon:
            power += self.weapon.damage
        return power

    # Método para mover al jugador a otra habitación
    def move(self, direction):
        # Verifica si la dirección es una salida válida
        if direction in self.current_room.exits:
            next_room_info = self.current_room.exits[direction]
            # Verifica si la salida no está bloqueada
            if not next_room_info["locked"]:
                self.current_room = next_room_info["room"]  # Cambia de habitación
                print(f"Te mueves hacia el {direction}.")
                self.look()  # Muestra la descripción de la nueva habitación
            else:
                # Mensaje específico si la puerta del trono está bloqueada
                if next_room_info.get("key") == "Scepter":
                    print("Una barrera mágica bloquea tu camino. Solo un símbolo de poder puede pasar.")
                else:
                    print("El camino está bloqueado.")
        else:
            print("No puedes ir en esa dirección.")

    # Método para que el jugador tome un objeto
    def take_item(self, item_name):
        item_to_take = None
        # Busca el objeto en la habitación actual
        for item in self.current_room.items:
            if item.name.lower() == item_name.lower():
                item_to_take = item
                break
        
        # Si encuentra el objeto, lo añade al inventario y lo quita de la habitación
        if item_to_take:
            self.inventory.append(item_to_take)
            self.current_room.items.remove(item_to_take)
            print(f"Tomas el {item_to_take.name}.")
            # Verifica si el objeto tomado es el que gana el juego
            if item_to_take.name == "Crown of Power":
                return "win"
        else:
            print(f"No hay {item_name} aquí.")
        return None

    # Método para que el jugador deje un objeto
    def drop_item(self, item_name):
        item_to_drop = None
        # Busca el objeto en el inventario
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                item_to_drop = item
                break
        
        # Si lo encuentra, lo quita del inventario y lo añade a la habitación
        if item_to_drop:
            self.inventory.remove(item_to_drop)
            self.current_room.items.append(item_to_drop)
            print(f"Dejas el {item_to_drop.name}.")
        else:
            print(f"No tienes un {item_name}.")

    # Método para mostrar el inventario del jugador
    def show_inventory(self):
        if not self.inventory:
            print("Tu inventario está vacío.")
        else:
            print("Llevas contigo:")
            for item in self.inventory:
                print(f"- {item.name} ({item.description})")

    # Método para que el jugador mire a su alrededor
    def look(self):
        print(f"\n--- {self.current_room.name} ---")
        print(self.current_room.description)
        # Muestra los objetos en la habitación
        if self.current_room.items:
            print("\nEn el suelo, ves:")
            for item in self.current_room.items:
                print(f"- Un {item.name}")
        # Muestra si hay una criatura en la habitación
        if self.current_room.creature:
            print(f"\n! Un {self.current_room.creature.name} está aquí! {self.current_room.creature.description}")
        
        print("\nSalidas:")
        # Muestra las salidas disponibles
        for exit_dir in self.current_room.exits:
            print(f"- {exit_dir}")
        
        print(f"\nTu salud: {self.health} HP")

    # Método para usar un objeto en una dirección
    def use_item(self, item_name, target_direction):
        item_to_use = None
        # Busca el objeto en el inventario
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                item_to_use = item
                break
        
        if not item_to_use:
            print(f"No tienes un {item_name}.")
            return

        # Verifica que la dirección de uso sea válida
        if target_direction not in self.current_room.exits:
            print(f"No puedes usar {item_name} en esa dirección.")
            return

        exit_info = self.current_room.exits[target_direction]
        # Si la salida está bloqueada y el objeto es la llave correcta, la desbloquea
        if exit_info.get("locked") and item_to_use.name == exit_info.get("key"):
            exit_info["locked"] = False
            print(f"Usas el {item_name} para desbloquear el camino hacia {target_direction}.")
        elif not exit_info.get("locked"):
             print("El camino ya está desbloqueado.")
        else:
            print(f"El {item_name} no parece funcionar aquí.")

    # Método para hablar con una criatura
    def talk_to_creature(self):
        if self.current_room.creature:
            print(self.current_room.creature.talk())
        else:
            print("No hay nadie con quien hablar aquí.")

    # Método para atacar a una criatura
    def attack_creature(self):
        creature = self.current_room.creature
        if not creature:
            print("No hay nada que atacar aquí.")
            return None

        if not self.weapon:
            print("¡Golpeas con tus propias manos!")
        
        # El jugador ataca a la criatura
        damage = self.attack_power
        print(f"¡Atacas al {creature.name} por {damage} de daño!")
        creature.health -= damage

        # Verifica si la criatura ha sido derrotada
        if creature.health <= 0:
            print(f"¡Has derrotado al {creature.name}!")
            # Si era el jefe, desbloquea la salida final
            if isinstance(creature, Boss):
                print("La barrera mágica hacia el sur parpadea y desaparece.")
                self.current_room.exits["south"]["locked"] = False
            self.current_room.creature = None  # Elimina a la criatura de la habitación
            
        else:
            print(f"Al {creature.name} le quedan {creature.health} HP.")
            # La criatura contraataca
            creature.attack(self)
            # Verifica si el jugador ha sido derrotado
            if self.health <= 0:
                return "lose" # Señal de fin de juego por derrota
        return None
        
# Define la clase para las habitaciones del juego
class Room:
    def __init__(self, name, description):
        self.name = name                # Nombre de la habitación
        self.description = description  # Descripción de la habitación
        self.exits = {}                 # Diccionario de salidas
        self.items = []                 # Lista de objetos en la habitación
        self.creature = None            # Criatura en la habitación (si la hay)

    # Método para añadir una salida a la habitación
    def add_exit(self, direction, room, locked=False, key=None):
        self.exits[direction] = {"room": room, "locked": locked, "key": key}

    # Método para añadir un objeto a la habitación
    def add_item(self, item):
        self.items.append(item)
        
    # Método para añadir una criatura a la habitación
    def add_creature(self, creature):
        self.creature = creature


# --- Configuración del Juego ---
# Creación de los objetos
key = Item("Key", "Abre una cerradura simple.", "key")
sword = Item("Sword", "Una confiable espada de acero.", "weapon", damage=15)
scepter = Item("Scepter of Power", "Brilla con una tenue energía mágica.", "key")
crown = Item("Crown of Power", "¡El premio final!", "misc")

# Creación de las criaturas
goblin = Creature("Goblin", "Un goblin maloliente.", 30, 8)
dragon_lord = Boss("Dragon Lord", "Un temible dragón cubierto de escamas negras.", 150, 25)

# Creación de las habitaciones
kitchen = Room("Cocina", "Estás en una cocina polvorienta.")
living_room = Room("Sala de estar", "Un viejo sofá yace en el centro.")
hallway = Room("Pasillo", "Un pasillo largo y oscuro.")
armory = Room("Armería", "Una pequeña habitación con estantes para armas.")
throne_room = Room("Salón del Trono", "Una gran sala con un trono imponente.")
treasure_room = Room("Sala del Tesoro", "Una habitación llena de oro y joyas. En el centro, un pedestal.")

# Colocar objetos y criaturas en las habitaciones
kitchen.add_item(key)
armory.add_item(sword)
throne_room.add_creature(dragon_lord)
throne_room.add_item(scepter) # El jefe suelta esto conceptualmente
treasure_room.add_item(crown)

# Conectar las habitaciones entre sí
kitchen.add_exit("sur", living_room)
living_room.add_exit("norte", kitchen)
living_room.add_exit("este", hallway, locked=True, key="Key")
living_room.add_exit("oeste", armory)
armory.add_exit("este", living_room)
hallway.add_exit("oeste", living_room)
hallway.add_exit("norte", throne_room)
throne_room.add_exit("sur", hallway, locked=True, key="Scepter of Power") # Inicialmente de un solo sentido


# --- Inicio del Juego ---
# Creación del jugador en la habitación inicial
player = Player("Héroe", kitchen)
print("=== ¡Bienvenido a la Mazmorra del Señor Dragón! ===")
print("Tu objetivo: Encuentra y reclama la Corona del Poder.")
print("Comandos: go <dir>, take <item>, drop <item>, use <item> <dir>, attack, talk, inv, look, quit")
player.look() # El jugador mira a su alrededor al empezar

# --- Bucle Principal del Juego ---
while True:
    # Comprueba si el jugador ha muerto
    if player.health <= 0:
        print("\n--- HAS MUERTO ---")
        sys.exit() # Termina el juego

    # Pide al jugador que introduzca un comando
    command = input("> ").lower().split()
    if not command:
        continue # Si no hay comando, vuelve a pedirlo
    
    action = command[0] # El primer elemento es la acción
    game_status = None  # Variable para rastrear el estado del juego (win/lose)

    # Evalúa la acción del jugador
    if action == "quit":
        print("¡Gracias por jugar!")
        break # Sale del bucle y termina el juego
    
    elif action == "go":
        if len(command) > 1:
            player.move(command[1])
        else:
            print("¿Ir a dónde?")

    elif action == "take":
        if len(command) > 1:
            game_status = player.take_item(" ".join(command[1:]))
        else:
            print("¿Tomar qué?")
            
    elif action == "drop":
        if len(command) > 1:
            player.drop_item(" ".join(command[1:]))
        else:
            print("¿Dejar qué?")

    elif action == "inv":
        player.show_inventory()

    elif action == "look" or action == "l":
        player.look()
        
    elif action == "use":
        if len(command) > 2:
            player.use_item(command[1], command[2])
        else:
            print("Usar <objeto> en <dirección> (ej. use key east)")
            
    elif action == "talk":
        player.talk_to_creature()

    elif action == "attack":
        game_status = player.attack_creature()

    else:
        print("No entiendo ese comando.")

    # Comprueba si el juego ha terminado (victoria o derrota)
    if game_status == "win":
        print("\n\n¡Felicidades! ¡Has reclamado la Corona del Poder y ganado el juego!")
        break
    elif game_status == "lose":
        print("\n--- HAS MUERTO ---")
        break
