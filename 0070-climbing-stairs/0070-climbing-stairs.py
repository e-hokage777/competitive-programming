class Solution(object):
    def __init__(self):
        self.memo = dict()

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 1:
            return 1
        if n == 2:
            return 2

        if n not in self.memo:
            self.memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)

        return self.memo[n]
        