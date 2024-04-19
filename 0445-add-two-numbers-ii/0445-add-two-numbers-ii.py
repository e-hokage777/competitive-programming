# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        l1 = self.reverse_list(l1)
        l2 = self.reverse_list(l2)

        return self.reverse_list(self.add(l1,l2))


    def reverse_list(self, head):
        prev = None
        current = head

        while current:
            temp = current.next
            current.next = prev

            prev = current
            current = temp

        return prev

    def add(self, l1, l2):
        sum_list = ListNode()
        current = sum_list
        carry = 0
        while l1 or l2:
            temp_sum = 0
            if l1:
                temp_sum += l1.val
                l1 = l1.next
            if l2:
                temp_sum += l2.val
                l2 = l2.next

            temp_sum += carry
            carry = temp_sum//10 ## getting carry
            temp_sum = temp_sum%10 ## getting remainder after carry

            current.next = ListNode(temp_sum)
            current = current.next

        if carry != 0:
            current.next = ListNode(carry)

        return sum_list.next ## sum_list is a dummy node hence the return

        