"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.nodes_equals(root.left, root.right)

    def nodes_equals(self, left, right):
        if (left and not right) or (not left and right):
            return False
        if not left and not right:
            return True
        if left.val != right.val:
            return False

        """
        First, it was my first comparison, 
        Runtime: 24 ms, faster than 54.07% of Python online submissions for Symmetric Tree.
        Memory Usage: 13.6 MB, less than 83.62% of Python online submissions for Symmetric Tree.
        if not self.nodes_equals(left.left, right.right):
            return False
        if not self.nodes_equals(left.right, right.left):
            return False
        """

        """
        Then, I did the comparison on the same if statement
        Runtime: 16 ms, faster than 94.98% of Python online submissions for Symmetric Tree.
        Memory Usage: 13.7 MB, less than 29.10% of Python online submissions for Symmetric Tree.
        """
        if not self.nodes_equals(left.left, right.right) or not self.nodes_equals(left.right, right.left):
            return False

        return True
