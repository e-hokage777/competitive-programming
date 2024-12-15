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

        def dfs(treenode, listnode):
            if not listnode:
                return True
            if not treenode:
                return False

            if treenode.val != listnode.val:
                listnode = head if head.val != treenode.val else head.next
                return dfs(treenode.left, listnode) or dfs(treenode.right, listnode)
            else:
                return dfs(treenode.left, listnode.next) or dfs(treenode.right, listnode.next)

        
        return dfs(root, head)
        