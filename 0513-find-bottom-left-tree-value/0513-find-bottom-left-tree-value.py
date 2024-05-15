# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
    
        def findMaxDepth(root, depth):
            if not root:
                return depth-1

            return max(findMaxDepth(root.left, depth+1), findMaxDepth(root.right, depth+1))

        max_depth = findMaxDepth(root, 1)

        deepest_lefts = []
        def findDeepestLeft(root, depth):
            if root == None:
                return

            if depth == max_depth:
                deepest_lefts.append(root.val)
            
            findDeepestLeft(root.left, depth+1)
            findDeepestLeft(root.right, depth+1)

        findDeepestLeft(root, 1)

        return deepest_lefts[0]
            