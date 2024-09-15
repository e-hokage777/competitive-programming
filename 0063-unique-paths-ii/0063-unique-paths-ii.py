class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        m,n = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[m-1][n-1]: return 0

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        dp[1][1] = 1
        
        for r in range(1, m+1):
            for c in range(1, n+1):
                if not obstacleGrid[r-1][c-1]:
                    dp[r][c] += dp[r-1][c] + dp[r][c-1]

        return dp[-1][-1]
        