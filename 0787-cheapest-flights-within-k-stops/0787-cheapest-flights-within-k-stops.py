from heapq import heappush, heappop
from collections import defaultdict
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        




        min_costs = [float("inf")] * n 
        min_costs[src] = 0


        for i in range(k+1):
            tmp_prices = min_costs[:]
            for _from, to, price in flights:
                if(min_costs[_from] == float("inf")):
                    continue
                tmp_prices[to] = min(tmp_prices[to], min_costs[_from] + price)

            min_costs = tmp_prices

        return min_costs[dst]



