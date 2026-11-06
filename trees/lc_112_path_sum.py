"""
LeetCode 112 - Path Sum
Difficulty: Easy
Category: Tree

Given the root of a binary tree and an integer targetSum,
return True if the tree has a root-to-leaf path such that
adding up all the values along the path equals targetSum.

A leaf is a node with no left or right child.

Example 1:

Input:
root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
targetSum = 22

Tree:

             5
            / \
           4   8
          /   / \
         11  13  4
        / \       \
       7   2       1

Output:
True

Explanation:
5 -> 4 -> 11 -> 2
5 + 4 + 11 + 2 = 22


Example 2:

Input:
root = [1, 2, 3]
targetSum = 5

Tree:

       1
      / \
     2   3

Output:
False


Example 3:

Input:
root = []
targetSum = 0

Output:
False
"""

def has_path_sum(root, targetSum):
    if not root:
        return False

    if not root.left and not root.right:
        return targetSum == root.val
    
    return has_path_sum(root.left, targetSum - root.val) or has_path_sum(root.right, targetSum - root.val)