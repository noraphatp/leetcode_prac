'''
Write a function build_graph(n, edges) that takes the number of vertices and a list of undirected edges, then returns an adjacency list.
'''


def build_graph(n, edges):
    graph = [[] for _ in range(n)]

    for u, v in edges:    
        graph[u].append(v)
        graph[v].append(u)

    return graph
    
n = 4
edges = [[0, 1], [0, 2], [1, 2], [2, 3]]

adj_list = build_graph(n,edges)
print(adj_list)