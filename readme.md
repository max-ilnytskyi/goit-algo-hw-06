# European Capitals Distance Network - Graph Algorithms

## Task 1: Graph Creation and Visualization

This project models a real-world network using the European capitals of Paris, London, Madrid, Berlin, and Milan. The graph is created as an undirected and unweighted network where edges represent connections between the capitals.

### Graph Details:
- **Number of nodes**: 5 (Paris, London, Madrid, Berlin, Milan)
- **Number of edges**: 9 (connections between cities)
- **Node degrees**: 
  - Paris: 4 (connected to London, Madrid, Berlin, and Milan)
  - London: 3 (connected to Paris, Berlin, and Milan)
  - Madrid: 3 (connected to Paris, Milan, and Berlin)
  - Berlin: 4 (connected to Paris, London, Madrid, and Milan)
  - Milan: 4 (connected to Paris, London, Madrid, and Berlin)

## Task 2: DFS and BFS Pathfinding

I implemented **Depth-First Search (DFS)** and **Breadth-First Search (BFS)** algorithms to find paths between two cities in the graph.

### Results:
- **DFS Path (Paris to Berlin)**: [Paris, Milan, Berlin]
- **BFS Path (Paris to Berlin)**: [Paris, Berlin]

### Comparison:

- **DFS**: DFS explores as deep as possible along each branch. It found a path from Paris to Berlin via Milan, which was not the shortest path.
- **BFS**: BFS explores neighbors level by level. It quickly found the direct path from Paris to Berlin, which is the shortest path in terms of the number of edges.

## Task 3: Implement Dijkstra's Algorithm for Shortest Path

In Task 3, I added weights (distances in kilometers) to the edges representing the distance between European capitals. I then implemented **Dijkstra’s Algorithm** to find the shortest path based on these weights.

### Results:
- **Dijkstra Path (Madrid to London)**: [Madrid, Paris, London]
- **Total Distance**: 1397 km

### Analysis:

Dijkstra's algorithm found the shortest path from Madrid to London, going through Paris. The total travel distance is 1397 kilometers, which is the minimal possible travel distance based on the graph's weights.
