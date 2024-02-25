class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """

        del_col_count = 0

        for j in range(len(strs[0])):
            current = strs[0][j]
            for i in range(1,len(strs)):
                if strs[i][j] >= current:
                    current = strs[i][j]
                else:
                    del_col_count += 1
                    break

        return del_col_count


        