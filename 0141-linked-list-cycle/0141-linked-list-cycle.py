# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        current = head

        while current:
            if current.val == None:
                return True
            
            current.val = None
            current = current.next

        return False
        