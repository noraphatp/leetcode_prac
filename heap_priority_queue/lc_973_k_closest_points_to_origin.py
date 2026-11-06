"""
LeetCode 973 - K Closest Points to Origin
Difficulty: Medium
Category: Heap / Priority Queue

You are given an array of points where:

points[i] = [x, y]

represents a point on a 2D plane.

Return the k points that are closest to the origin [0, 0].

The distance between a point [x, y] and the origin is:

sqrt(x^2 + y^2)

You may return the answer in any order.


Example 1:

Input:
points = [[1, 3], [-2, 2]]
k = 1

Distances:

[1, 3]:
sqrt(1^2 + 3^2) = sqrt(10)

[-2, 2]:
sqrt((-2)^2 + 2^2) = sqrt(8)

Output:
[[-2, 2]]


Example 2:

Input:
points = [[3, 3], [5, -1], [-2, 4]]
k = 2

Output:
[[3, 3], [-2, 4]]

The order of the returned points does not matter.
"""

import heapq

def k_closest(points, k):
    heap = []

    for (x, y) in points:
        dist = -(x*x + y*y)
        if len(heap) == k:
            # adds item to the heap then pops the smallest 
            heapq.heappushpop(heap, (dist, x, y))  
        else:
            heapq.heappush(heap, (dist, x, y))

    return [[x,y] for (dist, x, y) in heap]