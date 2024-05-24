from collections import OrderedDict
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        holder = OrderedDict()

        def traverse(node, col, row):
            if not node:
                return

            traverse(node.left, col-1, row+1)
            if col in holder:
                holder[col].append([col, row, node.val])
            else:
                holder[col] = [[col, row, node.val]]
            traverse(node.right, col+1, row+1)

        traverse(root, 0, 0)

        result = []

        for value in holder.values():
            value.sort()

            result.append([item[2] for item in value])

        return result
        