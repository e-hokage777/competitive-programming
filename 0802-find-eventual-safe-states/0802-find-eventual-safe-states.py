class Solution(object):
    UNVISITED = 0
    OPEN = 1
    CLOSED = 2

    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """

        colors = [Solution.UNVISITED] * len(graph)

        self.passed = []


        for node in range(len(graph)):
            if not colors[node]:
                colors[node] = Solution.OPEN
                self.dfs(graph, colors, node)
        
        return sorted(self.passed)


    def dfs(self, graph, colors, node):
        
        for child in graph[node]:
            if colors[child] == Solution.OPEN:
                return False
            if colors[child] == Solution.CLOSED:
                continue
            colors[child] = Solution.OPEN
            if not self.dfs(graph, colors, child): return


        colors[node] = Solution.CLOSED
        self.passed.append(node)
        return True



        