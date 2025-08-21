from collections import deque, defaultdict, Counter

EVEN = 0
ODD = 1

class Solution(object):
    def maxTargetNodes(self, edges1, edges2):
        """
        :type edges1: List[List[int]]
        :type edges2: List[List[int]]
        :rtype: List[int]
        """

        ## for each node in both trees, find odd counts
        ## if I know the odd counts, then I know the even
        ## for each query, connect each node in tree 1 to the node with the highest odd count
        ## in tree 2

        ## to find odd count for each node:
        ## even selected node level is even, all nodes on odd levels are have odd counts to it

        categories1 = self.compute_categories(edges1)
        categories2 = self.compute_categories(edges2)

        tree1_counts = Counter(categories1)
        tree2_counts = Counter(categories2)


        result = []

        for cat in categories1:
            if cat == EVEN:
                result.append(tree1_counts[EVEN] + max(tree2_counts.values()))
            else:
                result.append(tree1_counts[ODD] + max(tree2_counts.values()))

        return result


    def compute_categories(self, edges):
        '''
        function for getting binary list for each node
        0 for odd and 1 for even
        '''
        categories = [EVEN] * (len(edges) + 1)
        visited = [False] * (len(edges) + 1)

        ## form tree
        tree = defaultdict(list)

        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        queue = deque([0])
        visited[0] = 1
        level = 0

        while queue:
            level += 1
            length = len(queue)
            for i in range(length):
                current_node = queue.popleft()

                for child in tree[current_node]:
                    if not visited[child]:
                        if level % 2:
                            categories[child] = ODD
                        else:
                            categories[child] = EVEN

                        queue.append(child)
                        visited[child] = True

        return categories

        