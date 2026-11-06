"""
LeetCode: 209 - Minimum Size Subarray Sum
Pattern: Variable Sliding Window
Difficulty: Medium

Problem:
Given an array of positive integers nums and a positive
integer target, return the minimum length of a contiguous
subarray whose sum is greater than or equal to target.

If no such subarray exists, return 0.

Example:
target = 7
nums = [2, 3, 1, 2, 4, 3]

Output:
2

Explanation:
[4, 3] is the smallest valid subarray.

Time Complexity: O(n)
Space Complexity: O(1)

Key Idea:
Expand the window using right.

Once:
    window_sum >= target

the current window is valid.

Record its length and repeatedly shrink from the left
while it remains valid.

This allows us to find the smallest valid window.

Important:
Being inside:

    while window_sum >= target:

already guarantees that the current window is valid.
Therefore record its length BEFORE shrinking it.
"""

nums = [2, 3, 1, 2, 4, 3]
target = 7

def min_subarray_len(nums, target):
	left = 0
	window_sum = 0
	min_length = float("inf")

	for right in range(len(nums)):
		window_sum += nums[right]

		while window_sum >= target:
			min_length = min(min_length, right - left + 1)
			window_sum -= nums[left]
			left += 1

	return 0 if min_length == float("inf") else min_length 

print(min_subarray_len(target,nums))