class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        
        def dp(index, current_target):
            if current_target >= len(t):
                return 1
            if index >= len(s):
                return 0

            include = 0
            if s[index] == t[current_target]:
                include = dp(index+1, current_target+1)
            exclude = dp(index + 1, current_target)

            return include + exclude

        return dp(0,0)