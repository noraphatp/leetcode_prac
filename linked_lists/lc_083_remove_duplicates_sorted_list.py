"""
LeetCode 83 - Remove Duplicates from Sorted List
Difficulty: Easy
Category: Linked List

Given the head of a sorted linked list, delete all duplicates
such that each element appears only once.

Return the linked list sorted as well.

Example 1:

Input:
head = [1, 1, 2]

Output:
[1, 2]


Example 2:

Input:
head = [1, 1, 2, 3, 3]

Output:
[1, 2, 3]


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


def delete_duplicates(head):
    if not head:
        return []
    
    current = head

    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next

    return head

nums = [1, 1, 2, 2, 3, 4]

head = create_linked_list(nums)

print("Before:")
print_linked_list(head)

head = delete_duplicates(head)

print("After:")
print_linked_list(head)