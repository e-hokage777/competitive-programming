from collections import defaultdict, deque
class Solution(object):
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        """
        :type n: int
        :type redEdges: List[List[int]]
        :type blueEdges: List[List[int]]
        :rtype: List[int]
        """


        graph = defaultdict(list)
        level = 0
        result = [-1]*n

        for u,v in redEdges:
            graph[u].append((v,1))
            # graph[v].append((u,1))
        for u,v in blueEdges:
            graph[u].append((v,0))
            # graph[v].append((u,0))

        queue = deque([(0,1),(0,0)])
        visited = set()

        while queue:
            length = len(queue)
            for i in range(length):
                current, color = queue.popleft()
                result[current] = level
                for child,c in graph[current]:
                    if (current, child, color) in visited or c == color: continue
                    visited.add((current, child, color))
                    result[child] = level
                    queue.append((child,c))

            level += 1

        return result





        