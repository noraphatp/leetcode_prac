"""
LeetCode 141 - Linked List Cycle
Difficulty: Easy
Category: Linked List

Given head, the head of a linked list, determine whether the
linked list has a cycle in it.

A cycle exists if following the next pointers eventually causes
you to visit a node that you have already visited.

Return True if there is a cycle in the linked list.
Otherwise, return False.

Example 1:

Input:
head = [3, 2, 0, -4]
pos = 1

Output:
True

Explanation:
The tail connects back to the node at index 1.

3 -> 2 -> 0 -> -4
     ^          |
     |__________|


Example 2:

Input:
head = [1, 2]
pos = 0

Output:
True

Explanation:
The tail connects back to the node at index 0.

1 -> 2
^    |
|____|


Example 3:

Input:
head = [1]
pos = -1

Output:
False

Explanation:
There is no cycle.
"""

# two pointers
def has_cycle(head):
    fast = head
    slow = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            return True

    return False


# hash maps
def has_cycle_2(head):
    node_map = {}

    while head:
        if head in node_map:
            return True

        node_map[head] = True
        head = head.next

    return False


# set, cleaner version of hash maps 
def has_cycle_3(head):
    visited = set()

    while head:
        if head in visited:
            return True

        visited.add(head)
        head = head.next

    return False