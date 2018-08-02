# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# preorder traversal

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # recursive call, appends center, then left, then right node
        if root is not None:
            return ([root.val] + Solution.preorderTraversal(self, root.left) +
                    Solution.preorderTraversal(self, root.right))
        # base case
        else:
            return []


# inorder traversal

class Solution2:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # base case
        if root is None:
            return []
        # recursive call, combines left, then center, then right node
        else:
            return (self.inorderTraversal(root.left) + [root.val] +
                    self.inorderTraversal(root.right))


# postorder traversal

class Solution3:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # base case
        if root is None:
            return []
        # recursive call, combines left, then right, then center node
        else:
            return (self.postorderTraversal(root.left) +
                    self.postorderTraversal(root.right) + [root.val])
