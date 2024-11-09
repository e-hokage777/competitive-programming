class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.max_size = k
        self.size = 0
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """

        if self.size >= self.max_size: return False


        new_node = ListNode(value)
        
        # new_node.prev = self.head
        new_node.next = self.head.next
        if self.head.next: self.head.next.prev = new_node
        self.head.next = new_node

        if not self.tail.prev:
            self.tail.prev = new_node

        self.size += 1
        

        return True
        

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """

        if self.size >= self.max_size: return False

        new_node = ListNode(value)
        new_node.prev = self.tail.prev
        if self.tail.prev: self.tail.prev.next = new_node
        
        self.tail.prev = new_node

        if not self.head.next:
            self.head.next = new_node

        self.size += 1

        return True
        

    def deleteFront(self):
        """
        :rtype: bool
        """

        if not self.head.next:
            return False
        
        self.head.next = self.head.next.next

        if self.head.next:
            self.head.next.prev = None

        self.size -= 1

        if self.size == 0:
            self.tail.prev = None

        return True
        

    def deleteLast(self):
        """
        :rtype: bool
        """

        if not self.tail.prev:
            return False

        self.tail.prev = self.tail.prev.prev

        if self.tail.prev:
            self.tail.prev.next = None

        self.size -= 1

        if self.size == 0:
            self.head.next = None

        return True
        

    def getFront(self):
        """
        :rtype: int
        """

        return self.head.next.val if self.head.next else -1
        

    def getRear(self):
        """
        :rtype: int
        """

        return self.tail.prev.val if self.tail.prev else -1
        

    def isEmpty(self):
        """
        :rtype: bool
        """

        return not self.head.next
        

    def isFull(self):
        """
        :rtype: bool
        """

        return self.size == self.max_size
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()