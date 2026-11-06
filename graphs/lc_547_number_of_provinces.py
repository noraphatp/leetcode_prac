"""
LeetCode: 547 - Number of Provinces
Pattern: Graph / BFS / Connected Components
Difficulty: Medium

Problem:
There are n cities. Some cities are directly connected,
while others are not.

You are given an n x n adjacency matrix isConnected,
where isConnected[i][j] == 1 means city i and city j
are directly connected.

A province is a group of cities that are directly or
indirectly connected to each other.

Return the total number of provinces.

Example 1:
Input:
    isConnected = [
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 1]
    ]
Output: 2

Example 2:
Input:
    isConnected = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]
Output: 3

Time Complexity:
O(n^2) - For each visited city, BFS checks all n
possible neighbors by scanning its adjacency matrix
row. Each city is processed at most once.

Space Complexity:
O(n) - The visited set and BFS queue can each
contain up to n cities.

Key Idea:
Iterate through every city. Whenever an unvisited
city is found, increment the province count and
start BFS to visit all cities connected to it.

Each BFS explores one complete connected component,
which represents one province.
"""

from collections import deque

def findCircleNum(isConnected: list[list[int]]) -> int:
    n = len(isConnected)  
    visited = set()       
    provinces = 0         
    
    for city in range(n):
        if city not in visited:
            provinces += 1
            
            visited.add(city)

            queue = deque([city])

            while queue:
                curr = queue.popleft() # our current node

                for nei in range(n):
                    if isConnected[curr][nei] == 1 and nei not in visited:
                        visited.add(nei)
                        queue.append(nei)
            
            
    return provinces