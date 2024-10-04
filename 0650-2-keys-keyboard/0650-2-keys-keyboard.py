class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 0
        
        def dp(size, copy):
            if size > n:
                return float("inf")
            
            if size == n:
                return 1
            
            state = (size, copy)
            
            if state not in memo:
                memo[state] = min(2+dp(size+copy, size+copy), 1+dp(size+copy, copy))
            
            return memo[state]
        
        memo = dict()
        
        return dp(1,1)
        