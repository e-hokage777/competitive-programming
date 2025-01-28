class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        holder = dict()

        for char in s:
            holder[char] = holder.get(char, 0) + 1

        ans = 0
        max_odd = 0
        found_one = False
        for k, v in holder.items():
            if not v%2:
                ans += v
            else:
                ans += v-1
                found_one = True


        return ans + max_odd + found_one