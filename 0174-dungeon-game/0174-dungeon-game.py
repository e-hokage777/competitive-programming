class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """

        m,n = len(dungeon), len(dungeon[0])
        dp = [[0] * n for _ in range(m)]

        # if dungeon[0][0] < 1:
        #     dp[0][0] = -dungeon[0][0] + 1
        # else:
        #     dp[0][0] = 1

        dp[-1][-1] = max(-dungeon[-1][-1] + 1, 1)
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):

                left = float('inf')
                top = float("inf")

                if j < n-1:
                    left = dp[i][j+1] - dungeon[i][j]
                if i < m-1:
                    top = dp[i+1][j] - dungeon[i][j]

                if dp[i][j] == 0:
                    dp[i][j] = min(max(left,1), max(top,1))

        return dp[0][0]


                

                    


        