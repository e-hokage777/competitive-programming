class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        ans = []
        holder = []
        self.s = s

        def recurse(left, right):
            current_substring = s[left:right+1]

            if left >= len(self.s):
                return
            if right >= len(self.s):
                if self.is_palindrome(current_substring):
                    ans.append(holder[:] + [current_substring])
                return
            

            if self.is_palindrome(current_substring):
                holder.append(current_substring)
                recurse(right+1, right+1)
                holder.pop()
            recurse(left, right+1)


        recurse(0,0)

        return ans

    def is_palindrome(self, string):
        left = 0
        right = len(string) - 1

        while left < right:
            if string[left] != string[right]:
                return False

            left += 1
            right -= 1

        return True
            
        