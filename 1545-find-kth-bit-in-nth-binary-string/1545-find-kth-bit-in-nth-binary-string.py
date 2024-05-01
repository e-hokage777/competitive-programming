class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        s = ["0"]

        for i in range(1,n):
            if len(s) >= k:
                return s[k-1]
                
            s += ["1"] + self.reverse_invert(s)

        return s[k-1]

    def reverse_invert(self, s):
        return ["1" if s[i] == "0" else "0" for i in range(len(s)-1,-1,-1)]

        