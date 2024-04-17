# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return None

        tortoise = head
        hare = head

        if head.next:
            hare = hare.next.next
            tortoise = head.next
        else:
            return None

        while hare and tortoise != hare:
            if hare.next:
                tortoise = tortoise.next
                hare = hare.next.next
            else:
                return None


        if not hare:
            return None

        
        hare = head

        while tortoise != hare:
            tortoise = tortoise.next
            hare = hare.next

        return hare
        