from heapq import heappush, heappop
class Solution(object):
    def totalCost(self, costs, k, candidates):
        """
        :type costs: List[int]
        :type k: int
        :type candidates: int
        :rtype: int
        """

        left_heap = []
        right_heap = []

        left = 0
        right = len(costs)-1

        total_cost = 0

        while left <= right and k > 0:
            if len(left_heap) == candidates and len(right_heap) == candidates:
                if left_heap[0] <= right_heap[0]:
                    total_cost += heappop(left_heap)
                    k -= 1
                else:
                    total_cost += heappop(right_heap)
                    k -= 1

            if left <= right and len(left_heap) != candidates:
                heappush(left_heap, costs[left])
                left += 1
            if left <= right and len(right_heap) != candidates:
                heappush(right_heap, costs[right])
                right -= 1

        while k > 0:
            if left_heap and right_heap:
                if left_heap[0] <= right_heap[0]:
                    total_cost += heappop(left_heap)
                    k -= 1
                else:
                    total_cost += heappop(right_heap)
                    k -= 1
            elif left_heap:
                total_cost += heappop(left_heap)
                k -= 1
            else:
                total_cost += heappop(right_heap)
                k -= 1

        return total_cost

        

        