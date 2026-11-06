"""
LeetCode 700 - Search in a Binary Search Tree
Difficulty: Easy
Category: Tree / Binary Search Tree

You are given the root of a binary search tree (BST) and an
integer val.

Find the node in the BST whose value equals val and return the
subtree rooted at that node.

If such a node does not exist, return None.

Example 1:

Input:
root = [4, 2, 7, 1, 3]
val = 2

Tree:

        4
       / \
      2   7
     / \
    1   3

Output:
[2, 1, 3]

Explanation:
The node with value 2 is found. Return that node, which represents
the subtree:

      2
     / \
    1   3


Example 2:

Input:
root = [4, 2, 7, 1, 3]
val = 5

Output:
None
"""

def search_bst(root, val):
    if not root:
        return None

    if root.val == val:
        return root

    if root.val > val:
        return search_bst(root.left, val)
    else:
        return search_bst(root.right, val)