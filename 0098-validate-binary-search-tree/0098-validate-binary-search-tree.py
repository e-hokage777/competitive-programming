# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def validate(root, min_val, max_val):

            if not root:
                return True
            if root.val >= max_val or root.val <= min_val:
                return False
            if root.right and root.right.val <= root.val:
                return False
            if root.left and root.left.val >= root.val:
                return False


            return True and validate(root.left, min_val, min(root.val, max_val)) and validate(root.right, max(min_val, root.val), max_val)


        return validate(root, float("-inf"), float("inf"))

        
        