# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        dummy = ListNode(0)
        dummy.next = head
        current = head

        while current and current.next:
            if current.next.val < current.val:
                inserted = current.next
                lesser = dummy

                ## deleting pointer to next of current
                current.next = current.next.next
                while lesser.next.val < inserted.val:
                    lesser = lesser.next


                inserted.next = lesser.next
                lesser.next = inserted
                continue

            
            current = current.next

        return dummy.next
        