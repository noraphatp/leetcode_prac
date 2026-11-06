"""
LeetCode: 242 - Valid Anagram
Pattern: Hash Map / Frequency Counting
Difficulty: Easy

Problem:
Given two strings s and t, return True if t is an
anagram of s. Otherwise return False.

Example:
s = "anagram"
t = "nagaram"

Output:
True

Time Complexity: O(n)
Space Complexity: O(n)

Technically, if the input is restricted to a fixed alphabet
such as lowercase English letters, the space can be considered
O(1), because there can only be 26 keys.

Key Idea:
Count how many times each character appears in s.

Then go through t and subtract from those counts.

If a character doesn't exist or its count would become
invalid, the strings cannot be anagrams.
"""


def is_anagram(s, t):
    if len(s) != len(t):
        return False

    counts = {}

    for char in s:
        counts[char] = counts.get(char, 0) + 1

    for char in t:
        if char not in counts:
            return False

        counts[char] -= 1

        if counts[char] < 0:
            return False

    return True


s = "anagram"
t = "nagaram"

print(is_anagram(s, t))