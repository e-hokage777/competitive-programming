from collections import Counter, defaultdict
class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """

        if not len(s):
            return ""

        chars = set(s)

        for i in range(len(s)):
            if s[i].swapcase() not in chars:
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i+1:])

                return max(left, right, key=len)

        return s

        

        