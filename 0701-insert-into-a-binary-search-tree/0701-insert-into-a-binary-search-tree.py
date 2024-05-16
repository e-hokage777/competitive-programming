# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """


        def insert(root):
            if val < root.val and not root.left:
                root.left = TreeNode(val=val)
                return
            elif val > root.val and not root.right:
                root.right = TreeNode(val = val)
                return
            elif val < root.val:
                insert(root.left)
            else:
                insert(root.right)

        if root:
            insert(root)
        else:
            root = TreeNode(val=val)
        return root
        