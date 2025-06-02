# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        reversed_head = self.reverse(head)

        current_node = reversed_head


        while current_node:
            while current_node.next and current_node.next.val < current_node.val:
                temp = current_node.next.next
                current_node.next.next = None
                current_node.next = temp
            current_node = current_node.next

        return self.reverse(reversed_head)



    def reverse(self, head):
        current_node = None
        next_node = head

        while next_node:
            temp = next_node.next
            next_node.next = current_node

            current_node = next_node
            next_node = temp


        return current_node
        