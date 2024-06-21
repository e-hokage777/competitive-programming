# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self._sum = 0

        def dfs(current):
            if not current:
                return

            

            if not current.val%2:
                if current.left:
                    self._sum += current.left.left.val if current.left.left else 0
                    self._sum += current.left.right.val if current.left.right else 0
                if current.right:
                    self._sum += current.right.left.val if current.right.left else 0
                    self._sum += current.right.right.val if current.right.right else 0

            dfs(current.left)
            dfs(current.right)

        dfs(root)

        return self._sum

        