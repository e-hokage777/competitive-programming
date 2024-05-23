# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """

        if not root: return False
        def findPathSum(node, accumulation):
            if not node:
                return accumulation == targetSum

            return findPathSum(node.left, accumulation+node.val) or findPathSum(node.right, accumulation+node.val)

        return findPathSum(root, 0)
        