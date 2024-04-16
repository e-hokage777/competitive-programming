# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """

        leftPointer = head
        count=1
        while count < left:
            count+=1
            leftPointer = leftPointer.next
        
        holder=[]
        rightPointer = leftPointer
        diff = right-left
        count = 0
        while count <= diff:
            count+=1
            holder.append(rightPointer.val)
            rightPointer = rightPointer.next

        diff = right-left
        while diff >= 0:
            leftPointer.val = holder.pop()
            leftPointer = leftPointer.next
            diff-=1

        return head


        