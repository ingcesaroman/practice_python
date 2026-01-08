# Building a Restaurant Recommender for Mexico City: A Python Project

## Introduction

This project details the development of a basic restaurant recommendation system for Mexico City. Inspired by a Codecademy project, the goal was to create a command-line tool that suggests restaurant categories based on user input and then provides specific restaurant recommendations. The project focused on reinforcing key software engineering principles, including data structuring, algorithmic thinking, and version control.

## Data Collection

The initial approach involved web scraping Yelp.com for Mexico City restaurant data. However, due to the dynamic nature of website layouts and potential anti-scraping measures, directly scraping proved challenging with simple selectors. To ensure a robust dataset, a more pragmatic approach was adopted: leveraging Google web search results for "top [food type] restaurants in Mexico City." This allowed for the manual curation of a reliable list of popular establishments.

For this initial version, restaurant data was collected for several popular categories: "Tacos," "Mariscos" (Seafood), "Japonesa" (Japanese), "Café" (Coffee Shops), "Panaderías" (Bakeries), "Italiana" (Italian), "China" (Chinese), "Francesa" (French), and "India" (Indian), selecting 5-10 top-rated restaurants for each.

## Data Structure

The collected restaurant data is stored in a Python dictionary, `restaurants`, located in `data.py`. This dictionary's keys represent the food categories (e.g., "Tacos"), and each value is a list of restaurant dictionaries. Each inner restaurant dictionary contains at least a `'name'` and a `'description'`.

```python
# Example from data.py
restaurants = {
    'Tacos': [
        {'name': 'Los Cocuyos', 'description': 'Famous taqueria...'},
        # ... more taco restaurants
    ],
    'Mariscos': [
        {'name': 'Contramar', 'description': 'Renowned for its fresh seafood...'},
        # ... more seafood restaurants
    ],
    # ... other categories
}
```

This structure allows for efficient retrieval of recommendations based on the food type.

## Core Logic & Algorithms

The recommendation system's core logic resides in `recommender.py` and operates through a series of interconnected functions:

1.  **`greet()`:** Welcomes the user to the system and sets the context.
2.  **`show_food_types()`:** Iterates through the keys of the `restaurants` dictionary and displays the available food categories to the user.
3.  **`get_choice()`:** This is where the primary "search algorithm" is applied. It prompts the user for their desired food type. To enhance user experience, a simple **fuzzy matching algorithm** is implemented:
    *   If the user's input doesn't exactly match an available category, the function attempts to find a category that contains the user's input (case-insensitive).
    *   If a suggestion is found, the user is asked for confirmation. If confirmed, the suggested category is used.
    *   If no exact match or confirmed suggestion is found, the user is prompted to re-enter their choice.
4.  **`show_recommendations(food_type)`:** Takes the confirmed `food_type` and iterates through the corresponding list of restaurant dictionaries in the `restaurants` data structure, printing each restaurant's name and description.
5.  **`main()`:** Orchestrates the entire program flow, calling the above functions in a loop. It continuously asks for recommendations until the user decides to exit, providing a "¡Buen provecho!" message upon termination.

## How to Run the Program

To run the Mexico City Restaurant Recommender:

1.  **Ensure Python is installed:** This project requires Python 3.x.
2.  **Navigate to the project directory:** Open your terminal or command prompt and go to the `Portafolio_py/Algorithms/final_project_algorithms/restaurant_recommendation_system` directory.
3.  **Run the script:** Execute the command:
    ```bash
    python recommender.py
    ```
4.  **Interact:** Follow the prompts to enter your desired food type and receive recommendations. Try typing partial or slightly misspelled words to test the fuzzy matching!

## Future Improvements

While this version provides a solid foundation, several enhancements could be explored:

*   **Expanded Data:** Include more restaurants, additional food categories, and extra details like average rating, price range, address, and Yelp URL.
*   **More Sophisticated Fuzzy Matching:** Integrate libraries like `fuzzywuzzy` or `difflib` for more advanced string similarity comparisons.
*   **Filtering and Sorting:** Allow users to filter recommendations by rating, price, or specific amenities, and sort by various criteria.
*   **User Interface:** Develop a graphical user interface (GUI) using libraries like Tkinter, PyQt, or a web framework like Flask/Django for a more interactive experience.
*   **Advanced Recommendation Algorithms:** Implement collaborative filtering or content-based filtering if user preference data were available.
*   **Dynamic Data Fetching:** Instead of a static `data.py` file, integrate with the Yelp API (if permitted and feasible for a personal project) to fetch real-time data.

## Conclusion

This project successfully met its objectives by building a functional restaurant recommendation system, demonstrating the use of data structures and algorithms in a practical application. The experience reinforced the importance of clear data organization, robust user interaction design, and iterative development, all while maintaining good version control practices. It serves as a great starting point for more complex recommendation engines.
