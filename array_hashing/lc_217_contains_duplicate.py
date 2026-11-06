"""
LeetCode: 217 - Contains Duplicate
Pattern: Hash Set
Difficulty: Easy

Problem:
Given an integer array nums, return True if any value
appears at least twice. Otherwise return False.

Example:
nums = [1, 2, 3, 1]

Output:
True

Time Complexity: O(n)
Space Complexity: O(n)

Key Idea:
Keep a set containing numbers we have already seen.

Before adding a number, check whether it is already
in the set.

Set lookup is O(1) average time.
"""


def contains_duplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True

        seen.add(num)

    return False


nums = [1, 2, 3, 1]

print(contains_duplicate(nums))