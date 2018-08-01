# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        top = TreeNode(preorder[0])
        # print("PO: " + str(preorder))
        # print("IO: " + str(inorder))
        top_index = inorder.index(preorder[0])
        top.left = self.buildTree(
            preorder[1:(1 + top_index)], inorder[0:top_index])
        top.right = self.buildTree(
            preorder[(1 + top_index):], inorder[(top_index + 1):])

        return top
