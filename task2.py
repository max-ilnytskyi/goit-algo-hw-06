from task1 import G

def dfs(graph, start, goal, path=None):
    if path is None:
        path = []
    path.append(start)
    
    if start == goal:
        return path
    
    for neighbor in graph.neighbors(start):
        if neighbor not in path:
            result = dfs(graph, neighbor, goal, path)
            if result:
                return result
    path.pop()
    return None

def bfs(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for neighbor in graph.neighbors(vertex):
            if neighbor not in path:
                if neighbor == goal:
                    return path + [neighbor]
                else:
                    queue.append((neighbor, path + [neighbor]))
    return None

start_city = "Paris"
goal_city = "Berlin"

dfs_path = dfs(G, start_city, goal_city)
bfs_path = bfs(G, start_city, goal_city)

print(f"DFS Path from {start_city} to {goal_city}: {dfs_path}")
print(f"BFS Path from {start_city} to {goal_city}: {bfs_path}")
