"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes 
p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None 

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        # First case: Current node has p or q value.
        # It assumes than the other value is below of this.
        if root.val == p.val or root.val == q.val:
            return root
        
        # We check on left and right if one of the values is found
        # Both sites will found the first value available
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # Nothing on the both sides.
        if not left and not right:
            return None
        #Directly left and right have p and q. Root is parent 
        if left and right:
            return root
        # If we have something on left, but nothing in right, we assume than
        # we found something on left and the second one is
        # - on the other side on any other recursion
        # - below the left
        if left and not right:
            return left
        # FINAL SCENARIO
        # If we have something on right, but nothing in left, we assume than
        # we found something on right and the second one is
        # - on the other side on any other recursion
        # - below the right
        return right

        