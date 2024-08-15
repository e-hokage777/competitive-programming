class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        def dp(index, remainder):
            if remainder == 0:
                return 0

            if remainder < 0 or index >= len(coins):
                return float("inf")

            state = (index, remainder)
            if state not in memo:
                include = 1 + dp(index, remainder - coins[index])
                exclude = dp(index+1, remainder)

                memo[state] = min(include, exclude)

            return memo[state]

        memo = {}

        answer = dp(0,amount)

        return -1 if answer == float("inf") else answer
            
        