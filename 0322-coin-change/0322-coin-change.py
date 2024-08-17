class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        memo = {}
        memo[0] = 0
        def dp(value):

            if value not in memo:
                memo[value] = float("inf")
                for c in coins:
                    if c <= value:
                        memo[value] = min(memo[value], 1+dp(value-c))

            return memo[value]


        answer = dp(amount)

        return answer if answer != float("inf") else -1
            
        