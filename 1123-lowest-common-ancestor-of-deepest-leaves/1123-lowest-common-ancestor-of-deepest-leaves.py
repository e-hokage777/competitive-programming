from collections import deque, defaultdict

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        
        heights = defaultdict(int)
        parents = defaultdict(lambda: None)
        tree_nodes = defaultdict(lambda: None)
        queue = deque([root])


        height = 0

        while queue:
            length = len(queue)
            for i in range(length):
                node = queue.popleft()
                heights[node.val] = height
                tree_nodes[node.val] = node

                if node.left:
                    queue.append(node.left)
                    parents[node.left.val] = node.val
                if node.right:
                    queue.append(node.right)
                    parents[node.right.val] = node.val
            
            height += 1

        ## sort nodes by height to get lowest
        height_node_pairs = sorted(heights.items(), key = lambda x: x[1], reverse=True)


        ## getting lowest nodes
        lowest_height = height_node_pairs[0][1]
        lowest_nodes = []


        for i in range(len(height_node_pairs)):
            if height_node_pairs[i][1] == lowest_height:
                lowest_nodes.append(height_node_pairs[i][0])
            else:
                break


        if len(lowest_nodes) == 1:
            return tree_nodes[lowest_nodes[0]]

        while not self.check_same_parent(lowest_nodes, parents):
            for node in lowest_nodes:
                parents[node] = parents[parents[node]]

        lca = parents[lowest_nodes[0]]

        return tree_nodes[lca]

    def check_same_parent(self, nodes,parent_map):
        common_parent = parent_map[nodes[0]]
        for node in nodes:
            if parent_map[node] != common_parent:
                return False

        return True


        


            


        