"""
LeetCode: 20 - Valid Parentheses
Pattern: Stack
Difficulty: Easy

Problem:
Determine whether a string containing only brackets is valid.

A string is valid if:
- Every opening bracket has a matching closing bracket.
- Brackets are closed in the correct order.
- Each closing bracket matches the most recent unmatched
  opening bracket.

Example:
s = "({[]})"

Output:
True

Time Complexity: O(n)
Space Complexity: O(n)

Key Idea:
Use a stack to keep track of opening brackets.

When an opening bracket appears, push it onto the stack.

When a closing bracket appears, it must match the opening
bracket at the top of the stack.

If it does, pop the opening bracket.
If it doesn't, the string is invalid.

Because a stack is Last In, First Out (LIFO), the most
recent opening bracket must be the first one closed.

At the end, the stack must be empty for the string to be valid.
"""

s = "())"

def valid_brackets(s):
    s = s.replace(" ","")
    bracket_dict = {"}": "{", ")": "(", "]": "["}
    opening = ["{","(","["]
    closing = [")","}","]"]
    stack = []

    for bracket in s:
        # if first bracket is closing immediately return false
        if len(stack) == 0 and bracket in closing:
            return False

        if bracket in closing and bracket_dict[bracket] != stack[-1]:
            return False

        if bracket in opening:
            stack.append(bracket)
            continue

        if bracket_dict[bracket] == stack[-1]:
            stack.pop()
        
    return len(stack) == 0 

print(valid_brackets(s))