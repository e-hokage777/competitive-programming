import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        
        left = float("inf")
        right = float("-inf")

        for pile in piles:
            left = min(left, pile)
            right = max(right, pile)

        while left <= right:
            middle = left + (right - left)//2

            if self.can_finish(piles, middle, h):
                right = middle - 1
            else:
                left = middle + 1
                print("at else")


        return left


    def can_finish(self, piles, k, h):
        hours = 0

        for pile in piles:
            hours += int(math.ceil((pile * 1.0)/k))

        return hours <= h