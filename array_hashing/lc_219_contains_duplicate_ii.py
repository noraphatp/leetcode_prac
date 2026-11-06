"""
LeetCode: 219 - Contains Duplicate II
Pattern: Hash Map
Difficulty: Easy

Problem:
Given an integer array nums and an integer k,
return True if there are two distinct indices i and j
such that:

nums[i] == nums[j]

and:

abs(i - j) <= k

Example:
nums = [1, 2, 3, 1]
k = 3

Output:
True

Time Complexity: O(n)
Space Complexity: O(n)

Key Idea:
Store the most recent index where each number appeared.

When we encounter the same number again, compare the
current index with its previous index.

If the distance is <= k, return True.

Then update the number's most recent index.
"""


def contains_nearby_duplicate(nums, k):
    last_seen = {}

    for i in range(len(nums)):
        num = nums[i]

        if num in last_seen:
            if i - last_seen[num] <= k:
                return True

        last_seen[num] = i

    return False


nums = [1, 2, 3, 1]
k = 3

print(contains_nearby_duplicate(nums, k))