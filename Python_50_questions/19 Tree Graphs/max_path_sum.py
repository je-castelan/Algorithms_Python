"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any path.
"""

# Definition for a binary tree node.
 class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def __init__(self):
        self.res = -float("inf")

    def maxPathSum(self, root):
        self._navigate(root)
        return self.res
        
    def _navigate(self, root):
        if not root:
            return 0
        # The following recursion check the subpaths on left and right
        left = self._navigate(root.left)
        right = self._navigate(root.right)
        #Maxside check only the node and the max side
        maxside = max(root.val, max(left, right) + root.val)
        # Then, it will check sumarizing the node and BOTH sides
        maxtop = max(maxside, left + right + root.val)
        #Having two sides, it check if it is the max path
        self.res = max (self.res, maxtop)
        # It will return only the max side (not top) in order to check
        # upper on the tree
        return maxside
        
