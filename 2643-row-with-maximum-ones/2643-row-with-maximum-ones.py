class Solution(object):
    def rowAndMaximumOnes(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """

        max_count = 0
        max_row = 0
        for r in range(len(mat)):
            count = 0
            for c in range(len(mat[0])):
                count += mat[r][c]
            
            if count > max_count:
                max_count = count
                max_row = r

        return [max_row, max_count]

        