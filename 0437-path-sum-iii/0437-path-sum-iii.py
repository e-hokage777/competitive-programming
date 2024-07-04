# from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """

        # build graph
        nodes = []

        stack = [root]

        while stack:
            nodes.append(stack.pop())

            if(nodes[-1].left): stack.append(nodes[-1].left)
            if(nodes[-1].right): stack.append(nodes[-1].right)

        
        self.path_count = 0
        def dfs(current, current_sum):
            current_sum = current.val + current_sum
            if current_sum == targetSum:
                self.path_count += 1
            
            if current.left:
                dfs(current.left, current_sum)
            if current.right:
                dfs(current.right, current_sum)

        for node in nodes:
            dfs(node, 0)

        return self.path_count
        # self.target_path_count=0

        # def dfs(current, current_sum):

        #     self.target_path_count 

        #     current_sum = current.val + current_sum

        #     if current_sum == targetSum:
        #         self.target_path_count+=1
        #         current_sum = current.val

        #     if current_sum > targetSum:
        #         current_sum = current.val

        #     if current.left:
        #         dfs(current.left, current_sum)
        #     if current.right:
        #         dfs(current.right, current_sum)

        # dfs(root, 0)

        # return self.target_path_count
        