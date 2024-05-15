# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """


        self.result = []
        self.recursePreorder(root)
        return self.result

    def recursePreorder(self, root):
        if not root:
            return

        self.result.append(root.val)
        self.recursePreorder(root.left)
        self.recursePreorder(root.right)
        