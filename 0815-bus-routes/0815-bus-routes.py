from collections import defaultdict, deque
class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """

        if target == source: return 0

        graph = defaultdict(list)
        found = False
        for i in range(len(routes)):
            for j in range(len(routes[i])):
                graph[routes[i][j]].append(i)


        visited = set()
        queue = deque(graph[source])

        count = 0

        while queue:
            count += 1
            length = len(queue)

            for _ in range(length):
                current = queue.popleft()
                visited.add(current)

                for bus_stop in routes[current]:
                    if bus_stop == target: return count

                    for next_bus in graph[bus_stop]:
                        if next_bus not in visited: queue.append(next_bus)

        return -1


        

        
                
        
        