"""
LeetCode: 200 - Number of Islands
Pattern: Graph / BFS / Grid Traversal
Difficulty: Medium

Problem:
Given an m x n grid of characters where "1"
represents land and "0" represents water,
return the number of islands.

An island consists of horizontally or vertically
connected land cells. Diagonal connections
do not count.

Example 1:
Input:
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
Output: 1

Example 2:
Input:
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
Output: 3

Time Complexity:
O(n * m) - Every grid cell is examined a constant
number of times across the outer loops and BFS.

Space Complexity:
O(n * m) - The visited matrix and BFS queue.

Key Idea:
Scan the entire grid. Whenever an unvisited land
cell is found, increment the island count and
run BFS to mark all connected land cells as visited.

Each BFS represents one complete island.
"""

from collections import deque

def numIslands(grid):
    n = len(grid) # rows
    m = len(grid[0]) # columns

    islands = 0
    visited = [[False for _ in range(m)] for _ in range(n)]

    for r in range(n):
        for c in range(m):
            if grid[r][c] == "1" and not visited[r][c]: # key line
                islands += 1
                visited[r][c] = True
                queue = deque([(r,c)])

                while queue:
                    row, col = queue.popleft()

                    for x, y in [(row+1, col),(row-1, col),(row, col+1),(row, col-1)]:
                        if 0 <= x < n and 0 <= y < m and not visited[x][y] and grid[x][y] == "1":
                            queue.append((x,y)) 
                            visited[x][y] = True

    return islands