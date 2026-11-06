"""
LeetCode: 167 - Two Sum II
Pattern: Two Pointers
Difficulty: Medium

Problem:
Given a 1-indexed sorted array of integers, find two
numbers that add up to target.

Return their indices, adding 1 because the problem uses
1-based indexing.

Example:
numbers = [2, 7, 11, 15]
target = 9

Output:
[1, 2]

Time Complexity: O(n)
Space Complexity: O(1)

Key Idea:
Because the array is sorted, use pointers at both ends.

If the sum is too small:
    move left forward to increase the sum.

If the sum is too large:
    move right backward to decrease the sum.

If equal:
    return the indices.
"""


def two_sum(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]

        elif current_sum < target:
            left += 1

        else:
            right -= 1

    return []


numbers = [2, 7, 11, 15]
target = 9

print(two_sum(numbers, target))