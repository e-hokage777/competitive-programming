class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        max_candies = max(candies)

        return map(lambda x: x+extraCandies>=max_candies, candies)
        