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
        Assumption: traversals have all unique elements
        """
        # base case: empty list
        if not preorder:
            return None
        # uses the fact that the top node is always first element of
        # preorder traversal
        top = TreeNode(preorder[0])
        # gives the count of elements on the left side of tree
        top_index = inorder.index(preorder[0])
        # recursive call, builds left of tree using left side of traversals
        top.left = self.buildTree(
            preorder[1:(1 + top_index)], inorder[0:top_index])
        # recursive call, builds right of tree
        top.right = self.buildTree(
            preorder[(1 + top_index):], inorder[(top_index + 1):])

        return top
