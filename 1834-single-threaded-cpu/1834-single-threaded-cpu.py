import heapq
class Solution(object):
    def getOrder(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: List[int]
        """

        heap = []
        start_time = tasks[0][0]
        
        index = 0
        result = []
        
        while index < len(tasks):
            while index < len(tasks) and tasks[index][0] <= start_time:
                heappush(heap, (tasks[index][1], tasks[index][0], index))
                index+=1

            current = heappop(heap)

            start_time = current[0] + current[1]
            result.append(current[-1])

        for a in heap:
            result.append(a[-1])

        return result


        