# Strings (cadenas de texto)
nombre = "Python"
print(nombre)
print("Hola, " + nombre)  # Corrigiendo el uso de printf
print(nombre + " este es el lenguaje de python")

lenguaje = "JAVA"
print(lenguaje)
print(f"Hola, {lenguaje}")
print(f"{lenguaje} este es el nombre")

# Números (integers y floats)
edad = 25
altura = 1.75
print(f"Edad: {edad} años")
print(f"Altura: {altura} metros")

# Booleanos
es_programador = True
print(f"¿Es programador? {es_programador}")

# Listas
lenguajes = ["Python", "JavaScript", "Java"]
print("\nLenguajes de programación:")
for lenguaje in lenguajes:
    print(f"- {lenguaje}")