from functools import cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        @cache
        def min_coins(value):
            if value < 0:
                return float("inf")
                
            if value == 0:
                return 0

            min_count = float("inf")
            for coin in coins:
                remainder = value - coin
                candidate_count = min_coins(remainder) + 1

                if candidate_count < min_count:
                    min_count = candidate_count

            return min_count

        min_count =  min_coins(amount)

        if min_count == float("inf"):
            return -1

        return min_count

        