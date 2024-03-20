class Solution(object):
    def checkPalindromeFormation(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: bool
        """

        # for i in range(len(a)):
        #     if a[i] != b[len(a)-i-1]:
        #         if i >= len(a)-i-1 or self.isPalindrome(b[i:len(a)-i]):
        #             return True
        #         break
        #     if i >= len(a)-i-1:
        #         return True

        # for i in range(len(a)):
        #     # if i > len(a)-i-1:
        #     #     return True
        #     if  b[i] != a[len(b)-i-1]:
        #         if i >= len(a)-i-1 or self.isPalindrome(a[i:len(a)-i]):
        #             return True
        #         break

        #     if i >= len(a)-i-1:
        #         return True
                
        # return False



        l = 0
        r = len(a) - 1
        while l < r and a[l] == b[r]:
            l += 1
            r -= 1

        if l > r or self.isPalindrome(b[l:r+1]) or self.isPalindrome(a[l:r+1]):
            return True

        l = 0
        r = len(a) - 1
        while l < r and b[l] == a[r]:
            l += 1
            r -= 1

        if l > r or self.isPalindrome(a[l:r+1]) or self.isPalindrome(b[l:r+1]):
            return True

        return False

        

    def isPalindrome(self, s):
        l = 0
        r = len(s)-1

        while l <= r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True
        