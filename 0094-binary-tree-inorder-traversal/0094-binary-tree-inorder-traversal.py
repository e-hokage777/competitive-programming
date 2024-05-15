# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        result = []
        def recurseInorder(root):
            if not root:
                return

            recurseInorder(root.left)
            result.append(root.val)
            recurseInorder(root.right)

        recurseInorder(root)
        
        return result
        