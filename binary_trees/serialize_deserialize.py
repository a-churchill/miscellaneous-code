from collections import deque
import json


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return "[]"
        result = []
        result.append(root.val)
        next_node = deque()
        current = root
        # loops through all nodes
        # adds children to deque to parse next
        # adds their values to the result list, handling nulls appropriately

        # branch is ended (no longer needs nulls to represent empty spaces) if
        # its parent is null
        while current is not None:
            if current.left is not None:
                next_node.append(current.left)
                result.append(current.left.val)
            else:
                result.append("null")
            if current.right is not None:
                next_node.append(current.right)
                result.append(current.right.val)
            else:
                result.append("null")
            # print([node.val for node in next_node])
            if len(next_node) == 0:
                current = None
            else:
                current = next_node.popleft()

        # cleans result of extraneous "null" entries
        for i in range(len(result) - 1, 0, -1):
            if result[i] != "null":
                break
            else:
                result.pop()

        # print(str(result))
        return str(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # handles loading string as list, using JSON library
        if data == "[]":
            return None
        data = "{\"data\":" + data.replace("'", "\"") + "}"
        tree = deque(list(json.loads(data)["data"]))
        next_node = deque()
        root = TreeNode(tree.popleft())
        current = root
        while len(tree) > 0:
            val = tree.popleft()
            if val != 'null':
                current.left = TreeNode(val)
                next_node.append(current.left)
            if len(tree) == 0:
                break
            val = tree.popleft()
            current.right = TreeNode(val)
            next_node.append(current.right)
            current = next_node.popleft()
        return root
