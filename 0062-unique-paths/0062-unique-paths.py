class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        dp = [[0] * (n+1) for _ in range(m+1)]
        dp[1][1] = 1

        for r in range(1, m+1):
            for c in range(1,n+1):
                if not dp[r][c]:
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]
            
        return dp[-1][-1]