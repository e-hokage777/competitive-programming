from collections import defaultdict
from heapq import heappush, heappop
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """

        graph = defaultdict(list)

        k = k-1
        for source, target, time in times:
            graph[source-1].append((target-1, time))

        min_times = [float("inf") for _ in range(n)]
        min_times[k] = 0
        visited = [False]*n

        heap = [(0,k)]

        while heap:
            current_time, current_node = heappop(heap)
            visited[current_node] = True
            min_times[current_node] = min(min_times[current_node],current_time)
            
            for next_node, next_time in graph[current_node]:
                if not visited[next_node]:
                    new_time = current_time + next_time
                    heappush(heap, (new_time, next_node))

        
        min_time = max(min_times)

        return min_time if min_time != float("inf") else -1
            