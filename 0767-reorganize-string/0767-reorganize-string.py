from collections import Counter
from heapq import heappush, heappop
class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """


        counter = Counter(s)
        heap = [(-v,k) for k,v in counter.items()]
        heapify(heap)


        result = []
        while heap:
            current = heappop(heap)

            if not result:
                result.append(current[1])
                if current[0]+1:
                    heappush(heap, (current[0]+1, current[1]))
            else:
                if current[1] == result[-1]:
                    if heap:
                        _next = heappop(heap)
                        result.append(_next[1])
                        if _next[0] + 1:
                            heappush(heap, (_next[0]+1, _next[1]))
                    else:
                        return ""

                    heappush(heap, current)
                else:
                    result.append(current[1])
                    if current[0] + 1:
                        heappush(heap, (current[0]+1, current[1]))


        return "".join(result)



        






        