"""
LeetCode 876 - Middle of the Linked List
Difficulty: Easy
Category: Linked List

Given the head of a singly linked list, return the middle node
of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:

Input:
head = [1, 2, 3, 4, 5]

Output:
[3, 4, 5]

Explanation:
The middle node is node 3.


Example 2:

Input:
head = [1, 2, 3, 4, 5, 6]

Output:
[4, 5, 6]

Explanation:
There are two middle nodes, 3 and 4.
Return the second middle node, which is node 4.
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


def middle_node(head):
    fast = head
    slow = head

    while fast:
        fast = fast.next
        if fast != None:
            fast = fast.next
            slow = slow.next

    # alternate
    # while fast and fast.next:
    #     slow = slow.next
    #     fast = fast.next.next

    return slow


nums = [1, 2, 3, 4, 5]

head = create_linked_list(nums)
result = middle_node(head)

print_linked_list(result)