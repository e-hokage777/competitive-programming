class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """

        power = 1
        result = 0
        while num:
            if not num&1:
                result+=power
            num>>=1
            power*=2

        return result
        