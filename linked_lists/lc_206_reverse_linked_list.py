"""
LeetCode 206 - Reverse Linked List
Difficulty: Easy
Category: Linked List

Given the head of a singly linked list, reverse the list and
return the new head.

Example 1:

Input:
head = [1, 2, 3, 4, 5]

Output:
[5, 4, 3, 2, 1]


Example 2:

Input:
head = [1, 2]

Output:
[2, 1]


Example 3:

Input:
head = []

Output:
[]
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(nums):
    if not nums:
        return None

    head = ListNode(nums[0])
    current = head

    for num in nums[1:]:
        current.next = ListNode(num)
        current = current.next

    return head


def print_linked_list(head):
    current = head

    while current:
        print(current.val, end=" -> ")
        current = current.next

    print("None")


def reverse_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next # get next node with reference
        current.next = prev # reverse the pointer
        prev = current # move pointer to updated node
        current = next_node # move onto next node

    return prev


nums = [1, 2, 3, 4, 5]

head = create_linked_list(nums)

print("Before:")
print_linked_list(head)

head = reverse_list(head)

print("After:")
print_linked_list(head)