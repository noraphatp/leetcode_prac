"""
LeetCode: 733 - Flood Fill
Pattern: Graph / BFS / Matrix
Difficulty: Easy

Problem:
Given a 2D image, starting pixel (sr, sc), and a
new color, recolor the starting pixel and every
4-directionally connected pixel that has the
same original color.

Return the modified image.

Example 1:
Input:
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1, sc = 1, color = 2
Output:
    [[2,2,2],[2,2,0],[2,0,1]]

Time Complexity:
To be determined.

Space Complexity:
To be determined.

Key Idea:
To be determined after solving.
"""

from collections import deque


def floodFill(image, sr, sc, color):
    n = len(image) # rows
    m = len(image[0]) # columns

    initialColor = image[sr][sc]
    
    if initialColor == color:
        return image

    visited = [[None for _ in range(m)] for _ in range(n)]
    queue = deque([(sr,sc)])
    visited[sr][sc] = True

    while queue:
        sr, sc = queue.popleft()
        image[sr][sc] = color

        for x, y in [(sr+1,sc),(sr,sc+1),(sr,sc-1),(sr-1,sc)]:
            if 0 <= x < n and 0 <= y < m and not visited[x][y] and image[x][y] == initialColor:
                queue.append((x,y))
                visited[x][y] = True

    return image

