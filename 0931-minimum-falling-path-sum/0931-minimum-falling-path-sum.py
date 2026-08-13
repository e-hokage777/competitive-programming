class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """


        for row in range(1, len(matrix)):
            for col in range(len(matrix[0])):
                pos1, pos2, pos3 = float("inf"), float("inf"), float("inf")

                if col > 0:
                    pos1 = matrix[row][col] + matrix[row-1][col-1]
                if col < len(matrix[0])-1:
                    pos2 = matrix[row][col] + matrix[row-1][col+1]
                
                pos3 = matrix[row][col] + matrix[row-1][col]

                matrix[row][col] = min(pos1, pos2, pos3)

        return min(matrix[-1])




        