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
        if not head:
            return False

        current = head
        while current:
            if not hasattr(current, "next"):
                return True

            prev = current
            current = current.next
            del prev.next

        return False
        