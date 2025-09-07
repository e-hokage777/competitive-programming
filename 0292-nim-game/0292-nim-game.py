from collections import deque
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """

        return n < 4 or bool(n%4)
        