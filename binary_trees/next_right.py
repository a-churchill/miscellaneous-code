# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        node = root
        current = None
        candidate = None
        next_start = None
        if node is None:
            return
        while node is not None:
            # loop through nodes in this level, assigning nexts
            # assumption: previous level (node's level)
            # has all nexts assigned correctly

            # assign left's next to right if applicable
            if node.left is not None:
                # tells loop where to start for next level
                if next_start is None:
                    next_start = node.left

                if node.right is not None:
                    node.left.next = node.right
                    current = node.right
                else:
                    current = node.left
            else:
                if node.right is not None:
                    if next_start is None:
                        next_start = node.right
                    current = node.right
                else:
                    node = node.next
                    continue

            while candidate is None:
                node = node.next
                if node is None:
                    break
                if node.left is None:
                    if node.right is None:
                        continue
                    else:
                        candidate = node.right
                else:
                    candidate = node.left
            current.next = candidate
            candidate = None
            # end of inner loop, through nodes in a level
            if node is None:
                node = next_start
                next_start = None
