"""
LeetCode 19 - Remove Nth Node From End of List
Difficulty: Medium
Category: Linked List

Given the head of a linked list, remove the nth node from the
end of the list and return its head.

n is always valid.

Example 1:

Input:
head = [1, 2, 3, 4, 5]
n = 2

Output:
[1, 2, 3, 5]

Explanation:
The 2nd node from the end is 4, so node 4 is removed.


Example 2:

Input:
head = [1]
n = 1

Output:
[]


Example 3:

Input:
head = [1, 2]
n = 1

Output:
[1]
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

# two pass solution
# def remove_nth_from_end(head, n):
#     last = head
#     count = 0

#     while last:
#         last = last.next
#         count += 1

#     steps = count - n

#     if steps == 0:
#         head = head.next
#         return head

#     before_current = head
#     for i in range(steps - 1):
#         before_current = before_current.next

#     before_current.next = before_current.next.next

#     return head


def remove_nth_from_end(head, n):
    fast = head
    slow = head

    for i in range(n):
        fast = fast.next

    # remove first node case
    if not fast:
        return head.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next

    return head


nums = [1, 2, 3]
n = 3

head = create_linked_list(nums)

print("Before:")
print_linked_list(head)

head = remove_nth_from_end(head, n)

print("After:")
print_linked_list(head)