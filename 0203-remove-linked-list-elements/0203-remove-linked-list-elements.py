# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """

        new_head = None

        current = head
        new_head_current = None

        while current:
            if current.val != val:
                if not new_head:
                    new_head = ListNode(val = current.val)
                    new_head_current = new_head
                else:
                    new_head_current.next = ListNode(current.val)
                    new_head_current = new_head_current.next
            
            current = current.next

        return new_head


        