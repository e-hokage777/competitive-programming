from collections import deque, defaultdict
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """

        graph = defaultdict(list)

        for i in range(len(equations)):
            a,b = equations[i]
            graph[a].append((b,values[i]))
            graph[b].append((a,1/values[i]))


        def search(start, end):

            visited = set()
            queue = deque([(start,1)])

            while queue:
                current, current_val = queue.pop()
                visited.add(current)
                for child, val in graph[current]:
                    if child in visited: continue
                    if child == end: return current_val * val
                    queue.append((child, current_val * val))
            
            return -1

        result = []
        for a,b in queries:
            if not graph[a] or not graph[b]:
                result.append(-1)
            else:
                result.append(1 if a==b else search(a,b))

        return result
