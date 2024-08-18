class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """

        subproblems = [0]*(amount+1)
        subproblems[0] = 1
        for coin in coins:
            for value in range(coin, amount+1):
                subproblems[value] += subproblems[value-coin]

        return subproblems[-1]
        