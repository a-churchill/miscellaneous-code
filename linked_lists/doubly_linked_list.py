# structure of a node in a doubly linked list
class Node:

    def __init__(self, val, next_node=None, prev_node=None):
        """
        Node constructor, next and prev are optional
        """
        self.val = val
        self.next_node = next_node
        self.prev_node = prev_node

    def __str__(self):
        nn = "None" if self.next_node is None else str(self.next_node.val)
        pn = "None" if self.prev_node is None else str(self.prev_node.val)
        return "(Value: {0}, Next: {1}, Prev: {2})".format(self.val, nn, pn)


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list.
        If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        current = self.getNodeAtIndex(index)
        # print("Node retrieved: {0}".format(str(current)))
        if current is None:
            return -1
        else:
            return current.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node
        of the linked list.
        :type val: int
        :rtype: void
        """
        new_head = Node(val, self.head, None)
        if self.length == 0:
            self.tail = new_head
        else:
            self.head.prev_node = new_head
        self.head = new_head

        self.length += 1
        # print("Head: {0}".format(str(self.head)))
        # print("addAtHead result: {0}".format(str(self)))
        return

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        new_tail = Node(val, None, self.tail)
        if self.length == 0:
            self.head = new_tail
        else:
            self.tail.next_node = new_tail
        self.tail = new_tail
        self.length += 1
        # print("addAtTail result: {0}".format(str(self)))
        return

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list,
        the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        # if index is 0, add at head
        if index == 0:
            self.addAtHead(val)
            return
        elif index == self.length:
            self.addAtTail(val)
            return

        current = self.getNodeAtIndex(index)
        # current is set, now need to insert directly after it
        if current is None:
            return
        current = current.prev_node
        nn = Node(val, current.next_node, current)
        current.next_node = nn
        nn.next_node.prev_node = nn

        self.length += 1
        # print("addAtIndex result: {0}".format(str(self)))
        return

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        # validate input
        if index < 0:
            return
        elif index >= self.length:
            return
        # gets node to delete, updates references around it
        to_del = self.getNodeAtIndex(index)
        if to_del is None:
            return
        prevn = to_del.prev_node
        nextn = to_del.next_node
        if prevn is None:  # to_del is the head
            if nextn is None:  # list only has 1 elem
                self.head = None
                self.tail = None
            else:
                self.head = nextn
                nextn.prev_node = None
        elif nextn is None:  # to_del is the tail
            self.tail = prevn
            prevn.next_node = None
        else:  # to_del is in the middle of the list
            prevn.next_node = nextn
            nextn.prev_node = prevn

        self.length -= 1
        return

    def getNodeAtIndex(self, index):
        """
        Gets the node object at the given index
        O(1) at the edges, approaches O(n) in the middle
        (uses double sided nature)
        :type index: int
        :rtype: Node
        """
        # check input
        if index >= self.length:
            return None
        elif index < 0:
            return None
        # if element is closer to right side; better performance this way
        if index > self.length // 2:
            current = self.tail
            for i in range(self.length - 1, index, -1):
                if current is None:
                    return -1
                current = current.prev_node
        # if element is closer to left side
        else:
            current = self.head
            for i in range(index):
                if current is None:
                    return -1
                current = current.next_node

        return current

    # defines string representation of list
    def __str__(self):
        result = []
        current = self.head
        while current is not None:
            result.append(current.val)
            current = current.next_node

        return "MyLinkedList({0}, length {1})".format(str(result),
                                                      str(self.length))


# What is tested:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
