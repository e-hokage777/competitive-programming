class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        palindrome_found = [False] * len(s)
        max_start = 0
        max_end = 0
        for i in range(len(s)):
            j = len(s)-1
            while j > i:
                if palindrome_found[j]: break
                if s[i] == s[j]:
                    if self.check_palindrome(i, j, s):
                        if j - i > max_end - max_start:
                            max_start = i
                            max_end = j
                        palindrome_found[j] = True
                j-=1
        
        return s[max_start:max_end+1]

    def check_palindrome(self, start, end, s):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

        