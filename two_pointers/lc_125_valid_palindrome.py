"""
LeetCode: 125 - Valid Palindrome
Pattern: Two Pointers
Difficulty: Easy

Problem:
Determine whether a string is a palindrome after ignoring
non-alphanumeric characters and capitalization.

Example:
s = "A man, a plan, a canal: Panama"

Output:
True

Time Complexity: O(n)
Space Complexity: O(1)

Key Idea:
Put one pointer at each end.

Skip characters that aren't letters or numbers.

Compare the remaining characters.

If they differ, return False.
Otherwise move both pointers inward.
"""


def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:

        while left < right and not s[left].isalnum():
            left += 1

        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


s = "A man, a plan, a canal: Panama"

print(is_palindrome(s))