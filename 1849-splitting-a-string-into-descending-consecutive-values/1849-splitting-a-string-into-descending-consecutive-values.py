class Solution(object):
    def splitString(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def backtrack(index, array):
            ## base case
            if index >= len(s):
                for i in range(len(array) - 1):
                    if array[i] - array[i+1] != 1:
                        return False
                return len(array) > 1
            
            if len(array) > 1 and array[-1] - int(s[index:]) == 1:
                passed = True
                for i in range(len(array) - 1):
                    if array[i] - array[i+1] != 1:
                        passed = False
                        break

                if passed: return True

            for i in range(index, len(s)):
                array.append(int(s[index: i+1]))
                if backtrack(i+1, array):
                    return True
                array.pop()

            return False
        
        return backtrack(0, [])
        