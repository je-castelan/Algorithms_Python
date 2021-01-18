"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1(object):
    """
    This is my first solution
    Runtime: 20 ms, faster than 84.39% of Python online submissions for Binary Tree Level Order Traversal.
    Memory Usage: 14.2 MB, less than 20.22% of Python online submissions for Binary Tree Level Order Traversal.
    """
    def __init__(self):
        self.levels = []
        
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self._getValuesInLevel(root,0)
        return self.levels
    
    def _getValuesInLevel(self, node, level):
        if node:
            if len(self.levels) < level + 1:
                self.levels.append([node.val])
            else:
                self.levels[level].append(node.val)
            self._getValuesInLevel(node.left,level + 1)
            self._getValuesInLevel(node.right,level + 1)
        

class Solution2(object):
    def levelOrder(self, root):
        """
        Solution based on course 
        https://github.com/BitPunchZ/Leetcode-in-python-50-Algorithms-Coding-Interview-Questions/blob/master/Interview%20Questions%20solutions/Binary%20Tree%20Level%20Order%20Traversal/index.py
        Runtime: 24 ms, faster than 60.13% of Python online submissions for Binary Tree Level Order Traversal.
        Memory Usage: 13.8 MB, less than 72.06% of Python online submissions for Binary Tree Level Order Traversal.
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        solution = []
        if root:
            pendings = [root]
            tmp = []
            while pendings:
                n = len(pendings)
                for i in range(n):
                    node = pendings.pop(0)
                    tmp.append(node.val)
                    if node.left:
                        pendings.append(node.left)
                    if node.right:
                        pendings.append(node.right)
                if tmp:
                    solution.append(tmp[:])
                    tmp = []
        return solution
        