from collections import defaultdict

class Solution(object):
    def numSubmatrixSumTarget(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: int
        """

        count = 0

        for i in range(1,len(matrix[0])):
            matrix[0][i]+=matrix[0][i-1]
        for i in range(1,len(matrix)):
            matrix[i][0]+=matrix[i-1][0]
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                matrix[i][j] = matrix[i][j] + matrix[i][j-1] + matrix[i-1][j] - matrix[i-1][j-1]



        for r1 in range(len(matrix)):
            for r2 in range(r1, len(matrix)):
                holder = defaultdict(int)
                holder[0] = 1
                for c in range(len(matrix[0])):

                    if r1 == 0:
                        check = 0
                    else:
                        check = matrix[r1-1][c]

                    count += holder[target-matrix[r2][c]+check]

                    
                    holder[-matrix[r2][c] + (matrix[r1-1][c] if r1 > 0 else 0)]+=1

        return count





        