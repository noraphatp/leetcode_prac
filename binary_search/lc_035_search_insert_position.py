"""
LeetCode 35 - Search Insert Position
Difficulty: Easy
Category: Binary Search

Given a sorted array of distinct integers and a target value,
return the index if the target is found.

If the target is not found, return the index where it would be
inserted in order to keep the array sorted.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input:
nums = [1, 3, 5, 6]
target = 5

Output:
2


Example 2:

Input:
nums = [1, 3, 5, 6]
target = 2

Output:
1


Example 3:

Input:
nums = [1, 3, 5, 6]
target = 7

Output:
4
"""

def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left

    
nums = [1, 3, 5, 6]
target = 7
print(binary_search(nums,target))

# left is always in the correct position for insertion. also handles the case where nums is empty bc it just returns 0