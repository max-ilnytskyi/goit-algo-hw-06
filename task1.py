import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

capitals = ["Paris", "London", "Madrid", "Berlin", "Milan"]
G.add_nodes_from(capitals)

G.add_edges_from(
    [
        ("Paris", "London"),
        ("Paris", "Madrid"),
        ("Paris", "Berlin"),
        ("Paris", "Milan"),
        ("London", "Berlin"),
        ("London", "Milan"),
        ("Madrid", "Milan"),
        ("Madrid", "Berlin"),
        ("Berlin", "Milan"),
    ]
)


if __name__ == "__main__":
    plt.figure(figsize=(8, 6))
    nx.draw(
        G,
        with_labels=True,
        node_size=700,
        node_color="lightblue",
        font_size=10,
        font_weight="bold",
    )
    plt.title("European Capitals Network (Unweighted)")
    plt.show()

    num_nodes = G.number_of_nodes()
    num_edges = G.number_of_edges()
    degrees = dict(G.degree())

    print(f"Number of nodes: {num_nodes}")
    print(f"Number of edges: {num_edges}")
    print(f"Node degrees: {degrees}")
