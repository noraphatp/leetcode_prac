"""
LeetCode 226 - Invert Binary Tree
Difficulty: Easy
Category: Tree / DFS

Given the root of a binary tree, invert the tree and return its root.

Inverting a binary tree means swapping the left and right children
of every node.

Example 1:

Input:
root = [4, 2, 7, 1, 3, 6, 9]

Original:

        4
       / \
      2   7
     / \ / \
    1  3 6  9

Output:
[4, 7, 2, 9, 6, 3, 1]

Inverted:

        4
       / \
      7   2
     / \ / \
    9  6 3  1


Example 2:

Input:
root = [2, 1, 3]

Output:
[2, 3, 1]


Example 3:

Input:
root = []

Output:
[]
"""

def invert_tree(root):
    if not root:
        return None

    invert_tree(root.left)
    invert_tree(root.right)

    root.left, root.right = root.right, root.left

    return root


# tree = [4, 2, 7, 1, 3, 6, 9]