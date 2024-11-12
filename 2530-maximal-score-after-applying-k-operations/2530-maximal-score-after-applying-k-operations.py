from heapq import heapreplace, heapify
class Solution(object):
    def maxKelements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        heap=[-num for num in nums]
        heapify(heap)
        score = 0

        while k:
            score += -heap[0]
            heapreplace(heap, int(math.ceil(heap[0]/3)))
            k-=1
        return score
        