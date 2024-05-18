# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def find_leftmost(root):
            current = root
            while current.left:
                current = current.left
            
            return current.val

        def find_rightmost(root):
            current = root
            while current.right:
                current = current.right
            
            return current.val

        def search(root):
            if not root: return -1

            leftmost = find_leftmost(root)
            rightmost = find_rightmost(root)

            return max(
                abs(root.val-leftmost),
                abs(root.val-rightmost),
                search(root.left),
                search(root.right)
            )

        return search(root)
        