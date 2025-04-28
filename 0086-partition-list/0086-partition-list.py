# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """

    #     if not head:
    #         return head
        

    #     ## reverse linked
    #     ## arrange
    #     ## put back in order

    #     head = self.reverse_list(head)

    #     current_outer = head

    #     while current_outer:
    #         current_inner = current_outer

    #         while current_inner:
    #             if current_inner.next and current_inner.next.val > current_inner.val:
    #                 current_inner.next.val, current_inner.val = current_inner.val, current_inner.next.val

    #             current_inner = current_inner.next
            
    #         current_outer = current_outer.next

    #     return self.reverse_list(head)

    # def reverse_list(self, head):
    #     prev = None
    #     current = head

    #     while current:
    #         temp = current.next
    #         current.next = prev

    #         prev = current
    #         current = temp

    #     return prev

        if not head:
            return head

        values = []


        current = head

        while current:
            values.append(current.val)
            current = current.next


        for i in range(1, len(values)):
            j = i
            while j > 0 and values[j] <= values[j-1] and values[j-1] >= x and values[j] < x:
                values[j], values[j-1] = values[j-1], values[j]
                j-= 1

        return self.build_linked_list(values)

    
    def build_linked_list(self, values):
        head = ListNode(val = values[0])

        current = head

        for i in range(1, len(values)):
            current.next = ListNode(values[i])
            current = current.next

        return head

    # def list_len(self, head):
    #     current = head
    #     count = 0
    #     while current:

            