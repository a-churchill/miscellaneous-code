# Returns the node where the cycle in a singly linked list
# begins. If there is no cycle, returns None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # handle edge case: null list
        if head is None or head.next is None:
            return None
        current = head

        # uses O(1) lookup time of the dictionary for efficiency
        prevs = {str(current): 1}
        # mark last nodes
        while current.next is not None:
            next_node = current.next
            # print("Next node: {0}".format(str(next_node)))
            # checks if node was visited already
            if str(next_node) in prevs:
                return next_node
            prevs[str(next_node)] = 1
            current = next_node

        # reached end of list
        return None
