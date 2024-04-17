# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if not list1:
            return list2
        elif not list2:
            return list1

        prev1 = None
        current1 = list1
        prev2 = None
        current2 = list2
        current2_start = list2

        found=False
        while current1:
            while current2 and current2.val < current1.val:
                prev2 = current2
                current2 = current2.next
                found=True

            if found:
                if prev1:
                    prev1.next = current2_start
                else:
                    list1 = list2

                prev2.next = current1
                current2_start = current2
                found=False

            prev1 = current1
            current1 = current1.next

        if current2:
            prev1.next = current2_start

        # if list1.val >= list2.val:
        #     return list1
        
        # return list2
        return list1
        