import random
from random import randrange
from Graph import Graph
from Vertex import Vertex

def print_graph(graph):
  for vertex in graph.graph_dict:
    print("")
    print(vertex + " connected to")
    vertex_neighbors = graph.graph_dict[vertex].edges
    if len(vertex_neighbors) == 0:
      print("No edges!")
    for adjacent_vertex in vertex_neighbors:
      print("=> " + adjacent_vertex)

def build_tsp_graph(directed):
  g = Graph(directed)
  vertices = []
  for val in ['a', 'b', 'c', 'd']:
    vertex = Vertex(val)
    vertices.append(vertex)
    g.add_vertex(vertex)

  g.add_edge(vertices[0], vertices[1], 3)
  g.add_edge(vertices[0], vertices[2], 4)
  g.add_edge(vertices[0], vertices[3], 5)
  g.add_edge(vertices[1], vertices[0], 3)
  g.add_edge(vertices[1], vertices[2], 2)
  g.add_edge(vertices[1], vertices[3], 6)
  g.add_edge(vertices[2], vertices[0], 4)
  g.add_edge(vertices[2], vertices[1], 2)
  g.add_edge(vertices[2], vertices[3], 1)
  g.add_edge(vertices[3], vertices[0], 5)
  g.add_edge(vertices[3], vertices[1], 6)
  g.add_edge(vertices[3], vertices[2], 1)
  return g

# 3. Helper function to check if all vertices have been visited
def all_vertices_visited(visited_vertices):
  for vertex in visited_vertices:
    if visited_vertices[vertex] == "unvisited":
      return False
  return True

# 4. traveling_salesperson function
def traveling_salesperson(graph):
  # 4. Initialize path
  tsp_path = ""
  # 5. Initialize visited vertices dictionary
  visited_vertices = {x: "unvisited" for x in graph.graph_dict}
  
  # 6. Select a random starting vertex
  current_vertex = random.choice(list(graph.graph_dict.keys()))
  visited_vertices[current_vertex] = "visited"
  tsp_path += current_vertex

  # 7. Check if all vertices have been visited
  visited_all_vertices = all_vertices_visited(visited_vertices)

  # 8. Loop until all vertices have been visited
  while not visited_all_vertices:
    # 8. Get current vertex's edges
    current_vertex_edges = graph.graph_dict[current_vertex].edges
    # 9. Initialize variables for finding next vertex
    found_next_vertex = False
    next_vertex = ""

    # 10. Loop to find the next vertex
    while not found_next_vertex:
      # 11. Break if no more edges
      if not current_vertex_edges:
        break
      
      # 12. Find the minimum weight edge
      min_edge = min(current_vertex_edges, key=current_vertex_edges.get)
      
      if visited_vertices[min_edge] == "unvisited":
        found_next_vertex = True
        next_vertex = min_edge
      else:
        # Pop the visited edge and continue
        current_vertex_edges.pop(min_edge)

    # 13. Break outer loop if no next vertex found
    if not found_next_vertex:
      visited_all_vertices = True
    else:
      # 14. Move to the next vertex
      current_vertex = next_vertex
      visited_vertices[current_vertex] = "visited"
      tsp_path += " -> " + current_vertex

    # 15. Update loop condition
    visited_all_vertices = all_vertices_visited(visited_vertices)

  # 16. Print the final path
  print("Traveling Salesperson Path: " + tsp_path)

# 17. Build the graph and run the algorithm
tsp_graph = build_tsp_graph(False)
traveling_salesperson(tsp_graph)

