import math
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        l = 0
        r = math.floor(math.sqrt(c))
        while l <= r:
            pdt = l**2 + r**2
            if pdt == c:
                return True
            elif pdt > c:
                r -= 1
            else:
                l += 1

        return False


        