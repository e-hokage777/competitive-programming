from heapq import heappush, heappop, heapify
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """

        heap = [-stone for stone in stones]
        heapify(heap)

        while len(heap) > 1:
            first = -heappop(heap)
            second = -heappop(heap)

            if first != second:
                heaviest = max(first, second)
                less_heavy = min(first, second)

                heappush(heap, -(heaviest-less_heavy))

        if heap:
            return -heap[0]
        
        return 0


        