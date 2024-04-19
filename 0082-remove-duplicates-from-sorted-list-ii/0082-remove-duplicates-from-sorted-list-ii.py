# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        current = head
        found = False
        while current and current.next:
            while current and current.next and current.val == current.next.val:
                found=True
                current=current.next

            if found:
                prev.next = current.next
                current.next = None
                current = prev.next
                found=False
            else:
                current = current.next
                prev=prev.next



            
        return dummy.next
        