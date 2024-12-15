# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubPath(self, head, root):
        """
        :type head: Optional[ListNode]
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        # def dfs(treenode, listnode):
        #     if not listnode:
        #         return True
        #     if not treenode:
        #         return False

        #     if treenode.val != listnode.val:
        #         listnode = head if head.val != treenode.val else head.next
        #         return dfs(treenode.left, listnode) or dfs(treenode.right, listnode)
        #     else:
        #         return dfs(treenode.left, listnode.next) or dfs(treenode.right, listnode.next)

        
        # return dfs(root, head)

        stack = [root]

        while stack:
            current = stack.pop()

            if self.has_valid_path(current, head):
                return True
            
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)

        return False


    def has_valid_path(self, treenode, listnode):
        if not listnode:
            return True
        if not treenode:
            return False

        if treenode.val != listnode.val:
            return False
        else:
            return self.has_valid_path(treenode.left, listnode.next) or self.has_valid_path(treenode.right, listnode.next)
        