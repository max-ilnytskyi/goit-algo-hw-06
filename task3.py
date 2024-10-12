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
    return nx.dijkstra_path(graph, start, goal), nx.dijkstra_path_length(
        graph, start, goal
    )


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
