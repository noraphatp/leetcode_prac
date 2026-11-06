"""
Practice Problem: Maximum Sum Subarray of Size K
Pattern: Sliding Window (Fixed Size)
Difficulty: Easy

Problem:
Given an array of integers and an integer k, find the maximum
sum of any contiguous subarray of size k.

Example:
nums = [2, 1, 5, 1, 3, 2]
k = 3

Output:
9

Explanation:
The subarray [5, 1, 3] has the maximum sum of 9.

Time Complexity: O(n)
Space Complexity: O(1)

Key Idea:
Calculate the sum of the first window of size k.

Then slide the window one position at a time by subtracting
the element leaving the window and adding the new element
entering the window.

This avoids recalculating the entire sum for every window.
"""

nums = [2, 1, 5, 1, 3, 2]
k = 3

window_sum = sum(nums[i] for i in range(k))
max_sum = window_sum

for i in range(1, len(nums) - k + 1):
    window_sum = window_sum - nums[i-1] + nums[i+k-1]
    max_sum = max(max_sum, window_sum)

print(max_sum)