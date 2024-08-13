class Solution(object):
    def __init__(self):
        self.memo = dict()

    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 0: return 0
        if n == 1: return 1
        
        dp = [0]*(n+1)

        dp[0],dp[1] = 0, 1

        for index in range(2, n+1):
            dp[index] = dp[index-1] + dp[index-2]

        return dp[n]
        