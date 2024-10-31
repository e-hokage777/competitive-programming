from heapq import heappush, heappop
from collections import defaultdict
class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start_node: int
        :type end_node: int
        :rtype: float
        """

        visited = set()
        heap = [(-1,start_node)]
        probs = [0]*n
        probs[start_node] = 1

        edge_list = defaultdict(list)

        for i in range(len(edges)):
            edge_list[edges[i][0]].append((edges[i][1], succProb[i]))
            edge_list[edges[i][1]].append((edges[i][0], succProb[i]))

        while heap:
            current_prob, current_node = heappop(heap)
            visited.add(current_node)

            for neighbor_node, neighbor_prob in edge_list[current_node]:
                if neighbor_node not in visited:
                    new_prob = max(probs[neighbor_node],neighbor_prob * abs(current_prob))
                    probs[neighbor_node] = new_prob
                    heappush(heap, (-new_prob,neighbor_node))

        
        return probs[end_node]

        



        