# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        ## in case list is null
        if not head: return head

        ## getting length of linked list
        n = 0
        current = head

        while current:
            n+=1
            current = current.next

        ## removing cycles
        k = k%n

        ## no rotation or full rotation
        if k == 0: return head

        dummy_node = ListNode(0)
        dummy_node.next = head
        fast = dummy_node
        slow = dummy_node

        while k > 0:
            fast = fast.next
            k-=1

        while fast.next:
            fast = fast.next
            slow = slow.next

        fast.next = head
        head = slow.next
        slow.next = None

        return head


        