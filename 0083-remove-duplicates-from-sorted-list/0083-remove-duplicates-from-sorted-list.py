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
        current_num = -200

        while current:
            if current.val == current_num:
                prev.next = current.next
                current.next = None
                current = prev.next
            else:
                current_num = current.val
                prev = current
                current = current.next

            
        return dummy.next


        