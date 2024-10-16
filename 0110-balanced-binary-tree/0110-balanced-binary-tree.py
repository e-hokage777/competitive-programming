# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if not root: return True

        def traverse(node):
            if not node: return 0
            return max(1 + traverse(node.left), 1 + traverse(node.right))

        return abs(traverse(root.left) - traverse(root.right)) <= 1

            
        