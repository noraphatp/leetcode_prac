"""
LeetCode 98 - Validate Binary Search Tree
Difficulty: Medium
Category: Tree / Binary Search Tree

Given the root of a binary tree, determine whether it is a valid
binary search tree (BST).

A valid BST follows these rules:

1. Every node in a node's LEFT subtree must have a value LESS
   than that node's value.

2. Every node in a node's RIGHT subtree must have a value GREATER
   than that node's value.

3. Both the left and right subtrees must also be valid BSTs.

Example 1:

Input:
root = [2, 1, 3]

Tree:

      2
     / \
    1   3

Output:
True


Example 2:

Input:
root = [5, 1, 4, null, null, 3, 6]

Tree:

        5
       / \
      1   4
         / \
        3   6

Output:
False

Explanation:
The root is 5, but the node 4 is in the RIGHT subtree of 5.
Every node in the right subtree of 5 must be greater than 5.


Example 3:

Input:
root = [5, 4, 6, null, null, 3, 7]

Tree:

        5
       / \
      4   6
         / \
        3   7

Output:
False

Explanation:
3 is less than 5, but it appears inside 5's right subtree.
"""

def is_valid_bst(root):

    def check(root, min_val, max_val):
        if not root:
            return True
        if root.val <= min_val or root.val >= max_val:
             return False

        return check(root.left, min_val, root.val) and check(root.right, root.val, max_val)

    return check(root, float('-inf'), float('inf'))