class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        intervals.sort()

        end = intervals[0][-1]
        count_rem_intervals = 0

        print(intervals)

        for i in range(1, len(intervals)):
            current_start, current_end = intervals[i]

            ## if they overlap
            if current_start < end:
                count_rem_intervals += 1

                ## remove interval with largest endpoint
                end = min(end, current_end)
            else:
                end = current_end

        return count_rem_intervals
        