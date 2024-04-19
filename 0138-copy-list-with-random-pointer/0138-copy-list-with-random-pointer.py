"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        if not head: return None

        copy = ListNode(head.val)

        current = head
        current_copy = copy
        holder = {current: current_copy}

        ## first pass
        while current.next:
            current_copy.next = Node(current.next.val)

            current = current.next
            current_copy = current_copy.next

            holder[current] = current_copy


        ## second pass (copying randoms)
        current = head
        current_copy = copy


        while current:
            if current.random == None:
                current_copy.random = None
            else:
                current_copy.random = holder[current.random]

            current = current.next
            current_copy = current_copy.next


        return copy

        
        