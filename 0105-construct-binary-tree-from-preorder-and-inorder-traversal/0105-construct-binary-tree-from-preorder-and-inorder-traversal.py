# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """

        self.preorder = preorder
        self.inorder = inorder

        self.root_idx = 0
        def build_tree(left, right):
            if left > right: return None

            node = TreeNode()
            node.val = self.preorder[self.root_idx]

            if left == right: return node

            split_point = left
            for i in range(left, right+1):
                if self.inorder[i] == node.val:
                    split_point = i
                    break
            

            self.root_idx += 1
            node.left = build_tree(left, split_point-1)
            self.root_idx += 1
            node.right = build_tree(split_point+1, right)

            return node

        return build_tree(0, len(preorder)-1)

        