from data import restaurants

def greet():
    """Greets the user and explains the program."""
    print("Welcome to the Mexico City Restaurant Recommender!")
    print("I can recommend restaurants for the following types of food:")

def show_food_types():
    """Displays the available food types."""
    for food_type in restaurants:
        print(f"- {food_type}")

def get_choice():
    """Gets the user's choice of food type and validates it, with fuzzy matching."""
    available_food_types = list(restaurants.keys())
    choice = input("What type of food are you in the mood for? ").strip()

    while choice.title() not in available_food_types:
        # Simple fuzzy matching
        found_suggestion = False
        suggested_food_type = ""
        for food_type in available_food_types:
            if choice.lower() in food_type.lower():
                suggested_food_type = food_type
                found_suggestion = True
                break
        
        if found_suggestion:
            confirm = input(f"Did you mean '{suggested_food_type}'? (y/n) ").strip().lower()
            if confirm == 'y':
                return suggested_food_type
            else:
                print("No worries, let's try again.")
        else:
            print("I don't have recommendations for that. Please choose from the list above.")
        
        show_food_types() # Show food types again after an invalid/unconfirmed input
        choice = input("What type of food are you in the mood for? ").strip()
        
    return choice.title()

def show_recommendations(food_type):
    """Shows the restaurant recommendations for the chosen food type."""
    print(f"\nHere are some {food_type} restaurants in Mexico City:")
    for restaurant in restaurants[food_type]:
        print(f"- {restaurant['name']}: {restaurant['description']}")

def main():
    """Main function to run the recommender."""
    greet()
    while True:
        show_food_types()
        choice = get_choice()
        show_recommendations(choice)
        
        again = input("\nWould you like another recommendation? (y/n) ").strip().lower()
        if again != 'y':
            print("Enjoy your meal! ¡Buen provecho!")
            break

if __name__ == "__main__":
    main()