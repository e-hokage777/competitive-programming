class Solution(object):
    def matrixBlockSum(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

        ## handling the sum for the first column
        for i in range(1,len(mat[0])):
            mat[0][i] = mat[0][i] + mat[0][i-1]

        ## handling the sum for the first row
        for i in range(1, len(mat)):
            mat[i][0] = mat[i][0] + mat[i-1][0]

        ## handling the sum for the others
        for i in range(1, len(mat)):
            for j in range(1, len(mat[0])):
                mat[i][j] = mat[i][j] + mat[i][j-1] + mat[i-1][j] - mat[i-1][j-1]

        print(mat)

        result_matrix = [[0] *len(mat[0]) for i in range(len(mat))]

        for i in range(len(result_matrix)):
            for j in range(len(result_matrix[0])):
                r1 = max(i-k, 0)
                c1 = max(j-k, 0)
                r2 = min(len(mat)-1, i+k)
                c2 = min(len(mat[0])-1, j+k)

                pos_res = 0
                if r1 == 0 and c1 == 0:
                    pos_res =  mat[r2][c2]
                elif r1 == 0:
                    pos_res = mat[r2][c2] - mat[r2][c1-1]
                elif c1 == 0:
                    pos_res = mat[r2][c2] - mat[r1-1][c2]
                else:
                    pos_res = mat[r2][c2] - mat[r1-1][c2] - mat[r2][c1-1] + mat[r1-1][c1-1]

                result_matrix[i][j] = pos_res

        return result_matrix

        