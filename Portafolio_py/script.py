import random

class Player:
    """Represents a player in the game."""
    def __init__(self, name):
        self.name = name
        self.score = 0

class Game:
    """Manages the Rock, Paper, Scissors game logic."""
    def __init__(self, player1_name, player2_name="Computer"):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.choices = ["rock", "paper", "scissors"]

    def get_player_choice(self):
        """Gets and validates the player's choice."""
        while True:
            choice = input(f"{self.player1.name}, choose rock, paper, or scissors: ").lower()
            if choice in self.choices:
                return choice
            print("Invalid choice. Please choose again.")

    def get_computer_choice(self):
        """Gets the computer's random choice."""
        return random.choice(self.choices)

    def determine_winner(self, choice1, choice2):
        """Determines the winner of a round."""
        if choice1 == choice2:
            return "It's a tie!"
        
        winning_combinations = {
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper"
        }

        if winning_combinations[choice1] == choice2:
            self.player1.score += 1
            return f"{self.player1.name} wins this round!"
        else:
            self.player2.score += 1
            return f"{self.player2.name} wins this round!"

    def play_round(self):
        """Plays a single round of the game."""
        player1_choice = self.get_player_choice()
        player2_choice = self.get_computer_choice()

        print(f"{self.player1.name} chose: {player1_choice}")
        print(f"{self.player2.name} chose: {player2_choice}")

        result = self.determine_winner(player1_choice, player2_choice)
        print(result)
        self.display_scores()

    def display_scores(self):
        """Displays the current scores."""
        print("-" * 20)
        print("Scores:")
        print(f"{self.player1.name}: {self.player1.score}")
        print(f"{self.player2.name}: {self.player2.score}")
        print("-" * 20)

    def play_game(self):
        """Starts and manages the game loop."""
        print("Welcome to Rock, Paper, Scissors!")
        
        while True:
            self.play_round()
            
            play_again = input("Play another round? (yes/no): ").lower()
            if play_again != "yes":
                break
        
        print("Thanks for playing!")
        self.display_final_winner()

    def display_final_winner(self):
        """Displays the final winner of the game."""
        print("\n--- Final Score ---")
        self.display_scores()
        if self.player1.score > self.player2.score:
            print(f"Congratulations {self.player1.name}! You are the winner!")
        elif self.player2.score > self.player1.score:
            print(f"Sorry, {self.player2.name} is the winner. Better luck next time!")
        else:
            print("The game is a tie!")


if __name__ == "__main__":
    player_name = input("Enter your name: ")
    game = Game(player_name)
    game.play_game()
