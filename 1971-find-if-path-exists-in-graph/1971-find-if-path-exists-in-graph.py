from collections import defaultdict
class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        
        a_list = defaultdict(list)
        visited = set()
        for s,e in edges:
            a_list[s].append(e)
            a_list[e].append(s)

        def dfs(vertex):
            if vertex == destination:
                return True

            visited.add(vertex)
            for child in a_list[vertex]:
                if child in visited: continue
                if dfs(child):
                    return True
            return False

        return dfs(source)

