"""
LeetCode 1046 - Last Stone Weight
Difficulty: Easy
Category: Heap / Priority Queue

You are given an array of integers stones where stones[i]
is the weight of the ith stone.

Each turn, choose the two HEAVIEST stones and smash them together.

Suppose the two heaviest stones have weights x and y,
where x <= y.

If x == y:
    Both stones are destroyed.

If x != y:
    The stone of weight x is destroyed.
    The stone of weight y becomes weight y - x.

Continue until at most one stone remains.

Return the weight of the final remaining stone.
If no stones remain, return 0.

Example:

Input:
stones = [2, 7, 4, 1, 8, 1]

Process:

Heaviest: 8 and 7
8 - 7 = 1

stones effectively become:
[2, 4, 1, 1, 1]

Heaviest: 4 and 2
4 - 2 = 2

stones effectively become:
[2, 1, 1, 1]

Heaviest: 2 and 1
2 - 1 = 1

stones effectively become:
[1, 1, 1]

Heaviest: 1 and 1
both destroyed

stones:
[1]

Output:
1
"""

import heapq

def last_stone_weight(stones):
    for i in range(len(stones)):
        stones[i] = -stones[i]

    heapq.heapify(stones)

    while len(stones) > 1:
        first = -heapq.heappop(stones)
        second = -heapq.heappop(stones)
        if first != second:
            heapq.heappush(stones, -(first - second))

    return -stones[0] if stones else 0 