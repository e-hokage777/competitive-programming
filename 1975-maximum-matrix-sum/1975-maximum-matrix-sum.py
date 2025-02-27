class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        # a single zero can take care of any number of negatives
        # negative can be transferred to smallest positive
        # treat zeros as negatives
        negatives = []
        current_sum = 0
        smallest_num = float('inf')

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):

                if matrix[i][j] <= 0:
                    negatives.append(abs(matrix[i][j]))

                smallest_num = min(smallest_num, abs(matrix[i][j]))
                
                current_sum += abs(matrix[i][j])

        if not len(negatives) % 2:
            return current_sum
        return current_sum - 2*smallest_num

        
        