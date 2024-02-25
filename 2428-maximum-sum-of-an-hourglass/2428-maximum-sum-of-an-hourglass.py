class Solution(object):
    def maxSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        _max = -1
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                _sum = grid[i][j] + grid[i][j+1] + grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]

                if _sum > _max:
                    _max = _sum

        return _max
