"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""

class Solution(object):
    def __init__(self):
        self.signals = {'{': '}', '[': ']', '(': ')', }
        
    def isValid(self, s):
        """
        Runtime: 16 ms, faster than 88.74% of Python online submissions for Valid Parentheses.
        Memory Usage: 13.6 MB, less than 66.46% of Python online submissions for Valid Parentheses.
        
        :type s: str
        :rtype: bool
        """
        expected = []
        for l in s:
            if self.signals.get(l):
                expected.append(self.signals[l])
            else:
                if not expected:
                    return False
                elif l == expected[-1]:
                    expected.pop(-1)
                else:
                    return False
        if expected:
            return False
        return True