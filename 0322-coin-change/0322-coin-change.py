class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        memo = [float("inf") for _ in range(amount+1)]
        memo[0] = 0
        def dp(value):

            if memo[value] == float("inf"):
                for c in coins:
                    if c <= value:
                        memo[value] = min(memo[value], 1+dp(value-c))

            return memo[value]

        min_coins = float("inf")

        for i in range(amount+1):
            dp(i)

        return memo[-1] if memo[-1] != float("inf") else -1
            
        