"""
LeetCode 104 - Maximum Depth of Binary Tree
Difficulty: Easy
Category: Tree / DFS

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the
longest path from the root node down to the farthest leaf node.

Example 1:

Input:
root = [3, 9, 20, None, None, 15, 7]

Tree:

        3
       / \
      9   20
         /  \
        15   7

Output:
3


Example 2:

Input:
root = [1, None, 2]

Tree:

    1
     \
      2

Output:
2
"""

# initial solution
# def dfs(node, depth):
#     if not node:
#         return depth

#     depth += 1

#     return max(dfs(node.left, depth), dfs(node.right, depth))

# def max_depth(root):
#     if not root:
#         return 0 

#     return max(dfs(root.left, 1), dfs(root.right, 1))

def max_depth(root):
    if not root:
        return 0

    return 1 + max(max_depth(root.left), max_depth(root.right))