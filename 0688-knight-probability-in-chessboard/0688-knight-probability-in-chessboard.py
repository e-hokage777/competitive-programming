class Solution(object):
    def knightProbability(self, n, k, row, column):
        """
        :type n: int
        :type k: int
        :type row: int
        :type column: int
        :rtype: float
        """

        within_bounds = lambda r,c: r >= 0 and c >= 0 and r < n and c < n
        directions = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]
        memo = dict()


        def dp(row, col, k):
            if not within_bounds(row, col):
                return 0
            if k <= 0:
                return 1

            state = (row, col, k)

            if state in memo:
                return memo[state]

            moves = 0
            for dr, dc in directions:
                moves += dp(row+dr, col+dc, k-1)
            
            memo[state] = moves

            return memo[state]
        
        successes = dp(row, column, k) 
        return successes/8.0**k