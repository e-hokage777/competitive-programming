class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        r = len(matrix)
        c = len(matrix[0])
        transpose = [[0]*r for i in range(c)]
        for i in range(r):
            for j in range(c):
                transpose[j][i] = matrix[i][j]
                # if i > j:
                #     temp = matrix[i][j]
                #     matrix[i][j] = matrix[j][i]
                #     matrix[j][i] = temp

        return transpose
            