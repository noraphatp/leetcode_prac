"""
LeetCode 100 - Same Tree
Difficulty: Easy
Category: Tree / DFS

Given the roots of two binary trees p and q, determine whether
the two trees are the same.

Two binary trees are considered the same if they are structurally
identical and the nodes have the same values.

Example 1:

Input:
p = [1, 2, 3]
q = [1, 2, 3]

Trees:

      1             1
     / \           / \
    2   3         2   3

Output:
True


Example 2:

Input:
p = [1, 2]
q = [1, None, 2]

Trees:

      1             1
     /               \
    2                 2

Output:
False


Example 3:

Input:
p = [1, 2, 1]
q = [1, 1, 2]

Output:
False
"""

def is_same_tree(p, q):
    if not p and not q:
       return True

    if not p or not q:
        return False

    if p.val != q.val:
        return False

    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
