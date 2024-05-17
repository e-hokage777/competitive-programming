class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        min_so_far = float("inf")
        max_ = 0
        for price in prices:
            min_so_far = min(min_so_far, price)
            max_ = max(max_, price-min_so_far)

        return max_
        