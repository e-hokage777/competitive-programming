class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        self.head = None
        

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        current = self.head
        while current and index > 0:
            index-=1
            current = current.next

        if current:
            return current.value
        
        return -1

        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.head is None:
            self.head = Node(val)
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = Node(val)
        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index == 0:
            self.addAtHead(val)
            return 

        prev = None
        current = self.head
        new_node = Node(val)
        while current and index > 0:
            index -= 1
            prev = current
            current = current.next

        if current or index == 0:
            prev.next = new_node
            new_node.next = current
        

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """

        if index==0:
            self.head = self.head.next
            return

        prev=None
        current=self.head
        while current and index > 0:
            index -= 1
            prev = current
            current = current.next

        if current:
            prev.next = current.next

    def __repr__(self):
        current = self.head
        values = []
        while current:
            values.append(current.value)
            current = current.next
        
        return " ".join([str(v) for v in values])

        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)