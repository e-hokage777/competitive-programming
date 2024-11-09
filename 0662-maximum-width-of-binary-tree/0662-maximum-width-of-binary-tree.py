# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        max_dist = 0

        left = root.left
        right = root.right
        ld = 0
        rd = 0
        level_sum = 2

        while left and right:
            max_dist = max(max_dist, level_sum - rd - ld)

            level_sum*=2
            ld*=2
            rd*=2

            if left.left:
                left = left.left
            else:
                left = left.right
                ld += 1

            if right.right:
                right = right.right
            else:
                right = right.left
                rd += 1

        return max_dist


        