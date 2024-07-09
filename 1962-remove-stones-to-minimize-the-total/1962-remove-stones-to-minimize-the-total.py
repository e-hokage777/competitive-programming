import heapq
class Solution(object):
    def minStoneSum(self, piles, k):
        """
        :type piles: List[int]
        :type k: int
        :rtype: int
        """

        piles = [-pile for pile in piles]
        heapify(piles)

        while k:
            curr = heappop(piles)
            curr = curr//2
            heappush(piles, curr)

            k-=1

        return -sum(piles)

        