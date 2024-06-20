class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        marker = dict()
        def dfs(vertex, color):

            marker[vertex] = color

            for neighbor in graph[vertex]:
                if neighbor in marker and marker[neighbor] == color:
                    return False

                if neighbor in marker: continue

                if not dfs(neighbor, not color):
                    return False
        
            return True

        for i in range(len(graph)):
            if i not in marker:
                if not dfs(i, True): return False

        return True


        