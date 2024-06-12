# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        self.values = []
        self.inorderTraversal(root)


        return self.divide_and_conquer(0,len(self.values)-1)

    def divide_and_conquer(self, left, right):
        if left > right:
            return None

        mid = left + (right-left)//2
        left_child = self.divide_and_conquer(left, mid-1)
        right_child = self.divide_and_conquer(mid+1, right)

        current_node = TreeNode(self.values[mid], left_child, right_child)

        return current_node


    def inorderTraversal(self,root):
        if not root: return

        self.inorderTraversal(root.left)
        self.values.append(root.val)
        self.inorderTraversal(root.right)

        