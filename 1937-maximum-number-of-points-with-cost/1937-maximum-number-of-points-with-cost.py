class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        m = len(points)
        n = len(points[0])
        holder = [[0] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                if r == 0:
                    holder[r][c] = points[r][c]
                else:
                    max_value = 0
                    for cc in range(n):
                        val = points[r][c] + holder[r-1][cc] - abs(c - cc)
                        max_value = max(max_value, val)
                
                    holder[r][c] = max_value

        return max(holder[-1])
        