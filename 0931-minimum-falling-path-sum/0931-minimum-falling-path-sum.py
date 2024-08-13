class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        n = len(matrix)

        for r in range(n-2, -1, -1):
            for c in range(n):
                min_way = float("inf")
                current = matrix[r][c]
                if c < n-1:
                    min_way = min(min_way, current + matrix[r+1][c+1]) 
                if c > 0:
                    min_way = min(min_way, current + matrix[r+1][c-1]) 
                
                min_way = min(min_way, current + matrix[r+1][c])

                matrix[r][c] = min_way

        return min(matrix[0])
        