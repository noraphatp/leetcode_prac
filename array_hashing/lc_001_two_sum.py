"""
LeetCode: 1 - Two Sum
Pattern: Hash Map
Difficulty: Easy

Problem:
Given an array of integers nums and an integer target,
return the indices of two numbers that add up to target.

Example:
nums = [2, 7, 11, 15]
target = 9

Output:
[0, 1]

Time Complexity: O(n)
Space Complexity: O(n)

Key Idea:
Store numbers we have already seen in a hash map.

For each number:
    complement = target - current_number

If the complement has already been seen, we have found
the two numbers.

Hash map lookup is O(1) average time.
"""


def two_sum(nums, target):
    seen = {}

    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in seen:
            return [seen[complement], i]

        seen[nums[i]] = i

    return []


nums = [2, 7, 11, 15]
target = 9

print(two_sum(nums, target))