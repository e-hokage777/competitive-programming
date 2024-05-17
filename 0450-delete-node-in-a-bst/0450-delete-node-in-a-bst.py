# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """

        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:

            if not root.left:
                return root.right
            if not root.right:
                return root.left

            inorder_successor = self.find_inorder_successor(root.right)
            root.val = inorder_successor.val

            root.right = self.deleteNode(root.right, root.val)

        return root

    
    def find_inorder_successor(self, root):
        current = root
        while current.left:
            current = current.left

        return current


        
        