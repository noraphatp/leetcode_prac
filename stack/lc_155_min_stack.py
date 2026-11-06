"""
LeetCode: 155 - Min Stack
Pattern: Stack
Difficulty: Medium

Problem:
Design a stack that supports the normal stack operations while
also allowing the minimum value to be retrieved in constant time.

The stack must support:
- push(val): Add a value to the stack.
- pop(): Remove the top value.
- top(): Return the top value.
- getMin(): Return the minimum value.

All operations should run in O(1) time.

Example:
push(5)
push(2)
push(7)
push(1)

getMin() -> 1

pop()

getMin() -> 2

Time Complexity:
push()   -> O(1)
pop()    -> O(1)
top()    -> O(1)
getMin() -> O(1)

Space Complexity: O(n)

Key Idea:
Use two stacks.

The main stack stores every number.

The minimum stack only stores values that become a new minimum
(or are equal to the current minimum).

If a value is greater than the current minimum, we do not need
to store it in the minimum stack.

This works because stacks are Last In, First Out (LIFO).

Any larger values added after the current minimum must be popped
before that minimum can be removed. Therefore, those larger
values can never become the minimum while the smaller value is
still in the stack.

When the current minimum is eventually popped, remove it from
the minimum stack too. The previous minimum is then automatically
revealed underneath it.
"""

class MinStack:
    def __init__(self, nums: list[int] = None):
        self.nums = []
        self.min_nums = []

        if nums:
            for n in nums:
                self.push(n)

    def push(self, val: int) -> None:
        self.nums.append(val)

        if len(self.min_nums) == 0:
            self.min_nums.append(val)
        elif val <= self.min_nums[-1]:
            self.min_nums.append(val)

    def pop(self) -> None:
        if len(self.nums) != 0:
            val = self.nums.pop()
        if val == self.min_nums[-1]:
            self.min_nums.pop()

    def top(self) -> int:
        return self.nums[-1]

    def getMin(self) -> int:
        return self.min_nums[-1]

nums = [5, 2, 7, 1, 4]
stack = MinStack(nums)

print(stack.getMin())