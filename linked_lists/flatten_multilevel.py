"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

# Given a multilevel doubly linked list (some nodes have child pointer)
# flattens the list, inserting child lists in after their parent


class Solution:
    def flatten(self, head, first=None, top=None):
        """
        :type head: Node
        :rtype: Node
        """
        # handle first run
        if first is None:
            first = head

        # handle base case: null list
        if head is None:
            return None

        # track last node, for end of loop
        last_n = head
        # traverse as far as possible
        while head is not None:
            # handle if node has child; connect pointers
            if head.child is not None:
                next_n = head.next
                head.next = head.child
                head.next.prev = head
                head.child = None
                # recursive call to flatten any further children
                self.flatten(head.next, first, next_n)
            # step along list
            last_n = head
            head = head.next

        # connect end of current level to top (none if top level)
        last_n.next = top
        if last_n.next is not None:
            last_n.next.prev = last_n
        return first
