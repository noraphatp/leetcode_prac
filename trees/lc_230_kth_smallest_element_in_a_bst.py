"""
LeetCode 230 - Kth Smallest Element in a BST
Difficulty: Medium
Category: Tree / Binary Search Tree

Given the root of a binary search tree and an integer k,
return the kth smallest value among all the values in the tree.

k is 1-indexed:
k = 1 means the smallest value.
k = 2 means the second smallest value.
etc.

Example 1:

Input:
root = [3, 1, 4, null, 2]
k = 1

Tree:

        3
       / \
      1   4
       \
        2

Output:
1


Example 2:

Input:
root = [5, 3, 6, 2, 4, null, null, 1]
k = 3

Tree:

          5
         / \
        3   6
       / \
      2   4
     /
    1

Output:
3

Explanation:

The values in sorted order are:

1, 2, 3, 4, 5, 6

The 3rd smallest value is 3.
"""

def kth_smallest(root, k):

    def helper(root):
        nonlocal count

        if not root or count == 0:
            return

        helper(root.left)

        if count == 0:
            return

        count -= 1
        ar.append(root.val)

        if count == 0:
            return
        
        helper(root.right)

    ar = []
    count = k
    helper(root)

    return ar[-1]


def kth_smallest_iterative(root, k):
    stack = []
    current = root

    while True:
        # go to left most
        while current:
            stack.append(current)
            current = current.left

        node = stack.pop()
        k -= 1

        if k == 0:
            return node.val

        current = node.right