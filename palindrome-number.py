class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        x = str(x)

        l = 0
        r = len(x)-1

        while l <= r:
            if(x[l] != x[r]): return False
            l+=1
            r-=1

        return True
            
        
