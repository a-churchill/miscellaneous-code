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
        if root is not None:
            return ([root.val] + Solution.preorderTraversal(self, root.left) +
                    Solution.preorderTraversal(self, root.right))
        else:
            return []


# inorder traversal

class Solution2:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
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
        if root is None:
            return []
        else:
            return (self.postorderTraversal(root.left) + 
                    self.postorderTraversal(root.right) + [root.val])

