class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        def is_palindrome(left, right):
            temp = []
            while left < right:
                if (left, right) in memo: return True
                if s[left] != s[right]: return False
                left += 1
                right -= 1
                temp.append((left,right))

            for item in temp: memo[item] = True
            return True

        memo = dict()
        count = 0
        for i in range(len(s)):
            for j in range(i,len(s)):
                if s[i] == s[j] and is_palindrome(i,j):
                    count += 1

        return count
        