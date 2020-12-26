"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    My version
    Runtime: 40 ms, faster than 5.43% of Python online submissions for Maximum Depth of Binary Tree.
    Memory Usage: 16.3 MB, less than 26.62% of Python online submissions for Maximum Depth of Binary Tree.
    """
    def maxDepthv1(self, root):
        if not root:
            return 0
        return self._nextLevel(root, 1)
        
    def _nextLevel(self, node, prevlevel):
        if not node.left and not node.right:
            return prevlevel
        return max(
            self._nextLevel(node.left, prevlevel + 1) if node.left else 0, 
            self._nextLevel(node.right, prevlevel + 1) if node.right else 0
            )

    def maxDepthv2(self,root):
        """
        Checking the couse version, it's only neccesary one function

        Runtime: 32 ms, faster than 56.69% of Python online submissions for Maximum Depth of Binary Tree.
        Memory Usage: 16.1 MB, less than 80.81% of Python online submissions for Maximum Depth of Binary Tree.

        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        return max(
            self.maxDepthv2(root.left) + 1,  
            self.maxDepthv2(root.right) + 1
            )


if __name__ == "__main__":
    s = Solution()
    root1 = TreeNode(4, left = TreeNode(9), right=TreeNode(20, left = TreeNode(15), right=TreeNode(7)))
    print(s.maxDepthv1(root1))
    print(s.maxDepthv2(root1))
    root2 = TreeNode(1,right=TreeNode(2))
    print(s.maxDepthv1(root2))
    print(s.maxDepthv2(root2))