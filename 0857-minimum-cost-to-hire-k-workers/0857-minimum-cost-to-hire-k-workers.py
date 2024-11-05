from heapq import heappush, heappop
class Solution(object):
    def mincostToHireWorkers(self, quality, wage, k):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type k: int
        :rtype: float
        """

        ## step 1: sort according to wage per quality
        ## step 2: take subsequences of size k from left to right and use
        ##         greatest wage/quality as cap for increating lower ones
        ##         since quality is fixes, only way is to increase wage
        ##         which means new wage is bound to be higher then min wage
        ##         and ratios would meet conditions since we're trying to make
        ##         ratios the same

        wage_per_quality = [(wage[i]/(quality[i]*1.0), quality[i]) for i in range(len(wage))]

        wage_per_quality.sort()


        heap = []

        result = float("inf")
        quality_sum = 0
        current_ratio = 0
        for ratio, quality in wage_per_quality:
            if len(heap) == k and abs(heap[0]) > quality:
                q = heappop(heap)
                quality_sum -= abs(q)
                quality_sum += quality
                current_ratio=ratio
                heappush(heap, -quality)

            if len(heap) < k:
                heappush(heap, -quality)
                current_ratio = ratio
                quality_sum += abs(quality)

            if len(heap) == k:
                result = min(quality_sum * current_ratio, result)

        return result


        

        
            





        
        
        