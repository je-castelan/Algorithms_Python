"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        Runtime: 16 ms, faster than 92.23% of Python online submissions for Binary Tree Zigzag Level Order Traversal.
        Memory Usage: 13.6 MB, less than 70.94% of Python online submissions for Binary Tree Zigzag Level Order Traversal.
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        sol = []
        if root:
            pending = [root]
            sense = False
            while pending:
                tmp = []
                n = len(pending)
                for i in range(n):
                    element = pending.pop(0)
                    tmp.append(element.val)
                    if element.left:
                        pending.append(element.left)
                    if element.right:
                        pending.append(element.right)
                if tmp:
                    if not sense:
                        sol.append(tmp[:])
                    else:
                        sol.append(tmp[::-1])
                    tmp = []
                    sense = False if sense else True
        return sol