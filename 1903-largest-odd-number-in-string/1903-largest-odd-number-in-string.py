class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """

        for i in range(len(num)-1,-2, -1):
            if i < 0: return ""
            if int(num[i])%2:
                break

        return num[:i+1]
        