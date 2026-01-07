from graph_search import bfs, dfs
from vc_metro import vc_metro
from vc_landmarks import vc_landmarks
from landmark_choices import landmark_choices

from landmark_choices import landmark_choices

# Define landmark_string
landmark_string = ""
for letter, landmark in landmark_choices.items():
    landmark_string += f"{letter} - {landmark}\n"

# Define greet()
def greet():
    """
    Greets the user and displays the list of landmarks.
    """
    print("Hi there and welcome to SkyRoute!")
    print("We'll help you find the shortest route between the following Vancouver landmarks:\n" + landmark_string)

# 35. Add stations_under_construction list
stations_under_construction = ['Granville']

# 38-43. Implement get_active_stations()
def get_active_stations():
    """
    Generates an updated metro graph that accounts for station closures.
    """
    updated_metro = vc_metro.copy()
    for station_under_construction in stations_under_construction:
        for current_station, neighboring_stations in vc_metro.items():
            if current_station != station_under_construction:
                # Remove the closed station from the set of neighbors
                updated_metro[current_station] -= set(stations_under_construction)
            else:
                # Set the closed station's neighbors to an empty set
                updated_metro[current_station] = set([])
    return updated_metro

# 9-10. Implement get_start()
def get_start():
    """
    Gets the starting landmark from the user.
    """
    start_point_letter = input("Where are you coming from? Type in the corresponding letter: ")
    if start_point_letter in landmark_choices:
        start_point = landmark_choices[start_point_letter]
        return start_point
    else:
        print("Sorry, that's not a landmark we have data on. Let's try this again...")
        return get_start()

# 11. Implement get_end()
def get_end():
    """
    Gets the ending landmark from the user.
    """
    end_point_letter = input("Ok, where are you headed? Type in the corresponding letter: ")
    if end_point_letter in landmark_choices:
        end_point = landmark_choices[end_point_letter]
        return end_point
    else:
        print("Sorry, that's not a landmark we have data on. Let's try this again...")
        return get_end()

def set_start_and_end(start_point, end_point):
    """
    Sets the start and end points for the route calculation.
    """
    if start_point is not None:
        change_point = input("What would you like to change? You can enter 'o' for 'origin', 'd' for 'destination', or 'b' for 'both': ")
        if change_point == "b":
            start_point = get_start()
            end_point = get_end()
        elif change_point == "o":
            start_point = get_start()
        elif change_point == "d":
            end_point = get_end()
        else:
            print("Oops, that isn't 'o', 'd', or 'b'...")
            return set_start_and_end(start_point, end_point)
    else:
        start_point = get_start()
        end_point = get_end()
    return start_point, end_point

# 15-22 & 44-49. Implement get_route()
def get_route(start_point, end_point):
    """
    Finds the shortest route(s) between two landmarks.
    """
    start_stations = vc_landmarks[start_point]
    end_stations = vc_landmarks[end_point]
    routes = []
    for start_station in start_stations:
        for end_station in end_stations:
            # 44. Use updated metro graph if needed
            metro_system = get_active_stations() if stations_under_construction else vc_metro
            
            # 45-47. Check for possibility with DFS if stations are closed
            if stations_under_construction:
                possible_route = dfs(metro_system, start_station, end_station)
                if not possible_route:
                    continue

            # 49. Use the correct metro system for BFS
            route = bfs(metro_system, start_station, end_station)
            if route is not None:
                routes.append(route)
    
    # 48. Check if any routes were found
    if routes:
        shortest_route = min(routes, key=len)
        return shortest_route
    return None

# 31-32. Implement show_landmarks()
def show_landmarks():
    """
    Shows the list of landmarks if the user wants to see them again.
    """
    see_landmarks = input("Would you like to see the list of landmarks again? Enter y/n: ")
    if see_landmarks.lower() == 'y':
        print(landmark_string)

# 33. Implement goodbye()
def goodbye():
    """
    Prints a goodbye message.
    """
    print("Thanks for using SkyRoute!")

# 13-14, 24-29, 36-37. Implement new_route()
def new_route(start_point=None, end_point=None):
    """
    Manages the route creation and user interaction loop.
    """
    start_point, end_point = set_start_and_end(start_point, end_point)
    shortest_route = get_route(start_point, end_point)

    # 36. Check if a route exists
    if shortest_route:
        shortest_route_string = "\n".join(shortest_route)
        print("The shortest metro route from {0} to {1} is:\n{2}".format(start_point, end_point, shortest_route_string))
    # 37. Handle no route due to maintenance
    else:
        print("Unfortunately, there is currently no path between {0} and {1} due to maintenance.".format(start_point, end_point))

    again = input("Would you like to see another route? Enter y/n: ")
    if again.lower() == 'y':
        show_landmarks()
        new_route(start_point, end_point)

# 3, 27, 34, 50. Define skyroute()
def skyroute():
    """
    The main function for the SkyRoute program.
    """
    greet()
    new_route()
    goodbye()

# Call skyroute() to run the program
skyroute()