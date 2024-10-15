import networkx as nx
import matplotlib.pyplot as plt

from task1 import capitals


G_weighted = nx.Graph()

distances = {
    ("Paris", "London"): 343,
    ("Paris", "Madrid"): 1054,
    ("Paris", "Berlin"): 878,
    ("Paris", "Milan"): 639,
    ("London", "Berlin"): 930,
    ("London", "Milan"): 1208,
    ("Madrid", "Milan"): 1185,
    ("Madrid", "Berlin"): 1863,
    ("Berlin", "Milan"): 842,
}

start_city = "Madrid"
goal_city = "London"

G_weighted.add_nodes_from(capitals)

for (city1, city2), distance in distances.items():
    G_weighted.add_edge(city1, city2, weight=distance)


def dijkstra(graph, start, goal):
    adjacency_list = {node: {} for node in graph.nodes}
    for node1, node2, data in graph.edges(data=True):
        adjacency_list[node1][node2] = data["weight"]
        adjacency_list[node2][node1] = data["weight"]

    distances = {vertex: float("infinity") for vertex in adjacency_list}
    distances[start] = 0
    previous_nodes = {vertex: None for vertex in adjacency_list}
    unvisited = set(adjacency_list.keys())

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float("infinity"):
            break

        for neighbor, weight in adjacency_list[current_vertex].items():
            distance = distances[current_vertex] + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_vertex

        unvisited.remove(current_vertex)

        if current_vertex == goal:
            break

    path = []
    current_vertex = goal
    while current_vertex is not None:
        path.append(current_vertex)
        current_vertex = previous_nodes[current_vertex]
    path = path[::-1]

    return path, distances[goal]


dijkstra_path, dijkstra_cost = dijkstra(G_weighted, start_city, goal_city)

print(
    f"Dijkstra Path from {start_city} to {goal_city}: {dijkstra_path} with cost: {dijkstra_cost} km"
)

plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G_weighted)
nx.draw(
    G_weighted,
    pos,
    with_labels=True,
    node_size=700,
    node_color="lightgreen",
    font_size=10,
)
edge_labels = nx.get_edge_attributes(G_weighted, "weight")
nx.draw_networkx_edge_labels(G_weighted, pos, edge_labels=edge_labels)
plt.title("European Capitals Network with Distances")
plt.show()
