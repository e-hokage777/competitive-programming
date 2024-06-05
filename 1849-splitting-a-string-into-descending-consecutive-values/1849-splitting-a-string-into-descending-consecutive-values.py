class Solution(object):
    def splitString(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def backtrack(index, array):
            if len(array) > 1:
                if array[-2] - array[-1] != 1: return False
                if index >= len(s): return True
            

            for i in range(index, len(s)):
                array.append(int(s[index: i+1]))
                if backtrack(i+1, array):
                    return True
                array.pop()

            return False
        
        return backtrack(0, [])
        