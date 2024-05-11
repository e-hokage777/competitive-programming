class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        left = 0
        right = len(matrix) - 1


        while left < right:
            middle = left + (right - left)//2
            if matrix[middle][-1] >= target:
                right = middle
            else:
                left = middle + 1

        row = right

        left = 0
        right = len(matrix[row])-1
        while left <= right:
            middle = left + (right - left)//2

            if matrix[row][middle] == target:
                return True
            elif matrix[row][middle] > target:
                right = middle - 1
            else:
                left = middle + 1


        return False
        