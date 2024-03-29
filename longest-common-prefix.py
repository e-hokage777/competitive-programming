class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        ## case where only 1 string in list
        if len(strs) <= 1:
            return strs[0]
        
        index = 0
        end = False
        for char in strs[0]:
            for i in range(1, len(strs)):
                if len(strs[i])-1 <  index or strs[i][index] != char:
                    end = True
                    break

            index += 1

            if end: return strs[0][:index-1]

        return strs[0]
