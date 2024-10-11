# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        length = 0

        current = head
        while current:
            length += 1
            current = current.next


        for i in range(length):
            current = head
            for j in range(length-i):
                if current.next and current.val > current.next.val:
                    current.val, current.next.val = current.next.val, current.val

                current = current.next
                

        return head


        