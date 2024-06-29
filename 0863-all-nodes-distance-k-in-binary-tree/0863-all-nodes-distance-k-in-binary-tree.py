from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """

        level = 0
        level_dict = {root.val: level}
        side_dict = dict()
        queue = deque([root])

        if root.left:
            side_dict[root.left.val] =  True
        if root.right:
            side_dict[root.right.val] = False

        level += 1
        while queue:
            length = len(queue)

            for i in range(length):
                current = queue.popleft()
                if not current: break
                if current.left:
                    queue.append(current.left)
                    level_dict[current.left.val] = level
                    if current.left.val not in side_dict:
                        side_dict[current.left.val] = side_dict[current.val]
                if current.right:
                    queue.append(current.right)
                    level_dict[current.right.val] = level
                    if current.right.val not in side_dict:
                        side_dict[current.right.val] = side_dict[current.val]

            level += 1

        target = target.val
        result = []


        if target == root.val:
            for k,v in level_dict.items():
                if abs(level_dict[target]-v) == k:
                    result.append(k)
            return result

        target_side = side_dict[target]
        for key,v in level_dict.items():
            if key not in side_dict:
                if abs(v-level_dict[target]) == k:
                    result.append(key)
            elif side_dict[key] == target_side:
                if abs(v-level_dict[target]) == k:
                    result.append(key)
            else:
                if v + level_dict[target] == k:
                    result.append(key)

        return result
            