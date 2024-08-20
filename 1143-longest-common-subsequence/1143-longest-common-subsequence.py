class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """

        def dp(index1, index2):
            if index1 >= len(text1) or index2 >= len(text2):
                return 0

            state = (index1, index2)
            if state not in memo:
                include = int(text1[index1] == text2[index2])
                memo[state] = max(include+dp(index1+1, index2+1), dp(index1+1, index2),dp(index1, index2+1))

            return memo[state]

        memo = {}

        return dp(0,0)

        
        