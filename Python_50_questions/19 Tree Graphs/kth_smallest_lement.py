"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def kthSmallest(self, root, k):
        """
        Runtime: 36 ms, faster than 93.26% of Python online submissions for Kth Smallest Element in a BST.
    Memory Usage: 21.2 MB, less than 40.14% of Python online submissions for Kth Smallest Element in a BST.
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        
        if root:
            found = self.kthSmallest(root.left, self.k)
            if found is not None:
                return found
            if self.k == 1:
                return root.val
            else:
                self.k -= 1
            found = self.kthSmallest(root.right, self.k)
            if found is not None:
                return found
        else:
            return None