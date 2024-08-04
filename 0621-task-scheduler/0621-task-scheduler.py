from heapq import heappush, heappop
from collections import Counter, deque
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        counter = Counter(tasks)
        holder = []
        result = 0


        for _,v in counter.items():
            holder.append([0,-v])

        holder.sort(reverse=True)

        while holder:
            cool_off, count = holder.pop()
            count += 1
            result += max(cool_off,1)

            for i in range(len(holder)):
                holder[i][0] = max(holder[i][0]-cool_off, 0)

            if count < 0:
                holder.append([n, count])

            holder.sort(reverse=True)

        return result


        