# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        result = []

        def recursePostorder(root):
            if not root:
                return
            
            recursePostorder(root.left)
            recursePostorder(root.right)
            result.append(root.val)

        recursePostorder(root)

        return result
        