graph = [
    [1, 2], # node 0
    [0, 3], # node 1
    [0, 3], # node 2
    [1, 2]  # node 3
]

visited = set()

def dfs(node):
    visited.add(node)
    print(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor)

dfs(0)