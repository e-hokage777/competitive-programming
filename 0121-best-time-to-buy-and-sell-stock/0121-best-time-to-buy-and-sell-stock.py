class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        stack = []
        max_ = float("-inf")
        for price in prices:
            while stack and price < stack[-1]:
                max_ = max(max_, stack[-1] - stack[0])
                stack.pop()

            stack.append(price)

        return max(max_, stack[-1] - stack[0])
        