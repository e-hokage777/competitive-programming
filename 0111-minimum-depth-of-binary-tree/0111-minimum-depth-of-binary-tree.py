from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        if not root: return 0

        queue = deque([root])
        level = 1

        while queue:
            length = len(queue)

            for i in range(length):
                child = queue.popleft()
                if child.left:
                    queue.append(child.left)
                if child.right:
                    queue.append(child.right)
                if not child.left and not child.right:
                    return level
            level += 1


        