# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # key fact: if we keep going down the tree,
        # eventually one root we choose will be the LCA
        # so if we can recognize when the root is the LCA,
        # we can find the LCA recursively

        # base case 1: root is None
        if root is None:
            return None
        # base case 2: p or q is direct ancestor of other node
        if p.val == root.val or q.val == root.val:
            return root
        # recursive call: checks left and right for LCA
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # left or right will be None if root is not LCA
        # so if both are not None, root is LCA
        if left is not None and right is not None:
            return root
        # gets LCA from recursive call
        else:
            return left if left is not None else right
