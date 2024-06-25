from collections import deque, defaultdict
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        queue = deque([(root, 0)])
        holder = defaultdict(list)

        while queue:
            current, level = queue.popleft()

            if current:
                holder[level].append(current.val)

                if(current.left):
                    queue.append((current.left, level+1))
                if(current.right):
                    queue.append((current.right, level+1))

        result = []
        for _, l in sorted(holder.items(), key= lambda x: x[0]):
            result.append(l)

        return result
        