from collections import deque
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        if not root: return

        queue = deque([root])

        while queue:
            length = len(queue)
            for i in range(length):
                current = queue.popleft()
                current.next = queue[0] if i+1 < length else None

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)



        return root
        