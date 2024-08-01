from collections import defaultdict
class Solution(object):
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """

        graph = defaultdict(list)
        quiet_map = dict()

        for a,b in richer:
            graph[b].append(a)

        self.answer = [float("inf")] * len(quiet)


        for node in range(len(quiet)):
            if self.answer[node] == float("inf"):
                self.dfs(graph, node, quiet)

        for i,q in enumerate(quiet):
            quiet_map[q] = i

        return [quiet_map[x] for x in self.answer]

        

    def dfs(self, graph, node, quiet):
        if not graph[node]:
            self.answer[node] = quiet[node]
            return quiet[node]
        
        for child in graph[node]:
            if self.answer[child] != float("inf"):
                self.answer[node] = min(self.answer[child], self.answer[node], quiet[node])
            else:
                self.answer[node] = min(self.answer[node], self.dfs(graph,child, quiet), quiet[node])

        return self.answer[node]
        
        