from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        same_val = root.val
        queue = deque([root])

        while queue:
            current = queue.popleft()

            if current.left and current.left.val != same_val: return False
            if current.right and current.right.val != same_val: return False

            # queue.push(current.left)
            if current.left: queue.append(current.left)
            if current.right: queue.append(current.right)

        return True

        