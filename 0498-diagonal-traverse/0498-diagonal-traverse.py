class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        
        diagonals = defaultdict(lambda: [])
        diagonal_traversed = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                diagonals[i+j].append(mat[i][j])

        for k, v in diagonals.items():
            if k%2 == 0: ## add in reverse
                for i in range(len(v)-1, -1, -1):
                    diagonal_traversed.append(v[i])
            else: ## add in order
                for i in range(len(v)):
                    diagonal_traversed.append(v[i])

        return diagonal_traversed