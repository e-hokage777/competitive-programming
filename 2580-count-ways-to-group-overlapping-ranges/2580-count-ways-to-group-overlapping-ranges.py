class Solution(object):
    def countWays(self, ranges):
        """
        :type ranges: List[List[int]]
        :rtype: int
        """

        MOD = 10**9 + 7
        groups = 1

        ranges.sort()
        bound = ranges[0][1]

        for i in range(1, len(ranges)):
            if ranges[i][0] > bound:
                groups += 1
            
            bound = max(bound, ranges[i][1])

        print(ranges)
        return (2**groups)%MOD
        