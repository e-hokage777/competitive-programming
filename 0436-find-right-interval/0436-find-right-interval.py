class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """

        holder = dict()
        sorted_starts = []
        for idx, (s,_) in enumerate(intervals):
            holder[s] = idx
            sorted_starts.append(s)

        sorted_starts.sort()

        result = []

        for _, e in intervals:
            result.append(self.find_smallest_start(e, sorted_starts, holder))

        return result

    def find_smallest_start(self, end, starts, holder):
        left = -1
        right = len(starts)

        while right - left > 1:
            middle = left + (right - left)//2

            if starts[middle] >= end:
                right = middle
            else:
                left = middle

        if right == len(starts): return -1
        return holder[starts[right]]



        