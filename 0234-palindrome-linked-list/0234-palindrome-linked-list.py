# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        n=0

        current = head
        lastPointer=None
        while current:
            if not current.next:
                lastPointer = current
            n+=1
            current = current.next

        if n == 1:
            return True

        mid = n//2-1

        temp1 = head
        while mid > 0:
            mid-=1
            temp1 = temp1.next

        if n%2 == 0:
            temp2 = temp1.next
        else:
            temp2 = temp1.next.next

        temp1.next = None

        self.recurseReverse(temp2)
        temp2.next=None


        current1 = head
        current2 = lastPointer

        while current1:
            if current1.val != current2.val:
                return False

            current1 = current1.next
            current2 = current2.next

        return True


    def recurseReverse(self, current):
        if not current.next:
            return
        
        self.recurseReverse(current.next)
        current.next.next = current

        