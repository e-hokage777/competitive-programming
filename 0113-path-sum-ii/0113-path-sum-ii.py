# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """

        arr = []
        arr_sum = 0
        ans = []
        def recurse(node, arr, arr_sum):
                
            if not node.left and not node.right:
                if arr_sum == targetSum:
                    ans.append(arr[:])
                
                return

            if node.left:
                arr.append(node.left.val)
                arr_sum += node.left.val
                recurse(node.left, arr, arr_sum)

                arr.pop()
                arr_sum -= node.left.val

            if node.right:
                arr.append(node.right.val)
                arr_sum += node.right.val
                recurse(node.right, arr, arr_sum)

                arr.pop()
                arr_sum -= node.right.val


        if not root:
            return []
        recurse(root, [root.val], root.val)
        return ans

        