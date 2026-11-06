"""
LeetCode: 1971 - Find if Path Exists in Graph
Pattern: Graph / DFS
Difficulty: Easy

Problem:
Given an undirected graph with n vertices numbered
from 0 to n - 1, determine whether a valid path
exists from source to destination.

Return True if a path exists, otherwise False.

Example 1:
n = 3
edges = [[0, 1], [1, 2], [2, 0]]
source = 0
destination = 2

Output:
True

Example 2:
n = 6
edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
source = 0
destination = 5

Output:
False

Time Complexity:
To be determined.

Space Complexity:
To be determined.

Key Idea:
To be determined after solving.
"""


def validPath(n, edges, source, destination):
    graph = build_graph(n, edges)
    return dfs(graph, source, destination, set())

def build_graph(n, edges):
    graph = [[] for _ in range(n)]
    
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        
    return graph

def dfs(graph, src, dst, visited):
    if src == dst:
        return True
    
    visited.add(src)
    
    for neighbor in graph[src]:
        if neighbor not in visited:
            if dfs(graph, neighbor, dst, visited):
                return True
    
    return False
    


n = 3
edges = [[0, 1], [1, 2], [2, 0]]
source = 0
destination = 2

print(validPath(n, edges, source, destination))


# class Solution(object):
#     def validPath(self, n, edges, source, destination):
#         graph = [[] for _ in range(n)]

#         for u, v in edges:
#             graph[u].append(v)
#             graph[v].append(u)

#         visited = set([source])
#         stack = [source]

#         while stack:
#             node = stack.pop()

#             if node == destination:
#                 return True

#             for neighbor in graph[node]:
#                 if neighbor not in visited:
#                     visited.add(neighbor)
#                     stack.append(neighbor)

#         return False