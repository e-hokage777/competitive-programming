class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """

        checker = bool(n&1)

        while n:
            if checker != bool(n&1): return False
            n>>=1
            checker = not checker

        return True
        