class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        directions = [(-1,0), (1, 0), (0,-1), (0,1)]
        visited = [[0]*len(grid[0]) for _ in range(len(grid))]

        def dfs(row, col):
            if visited[row][col]:return 0

            perimeter = 0

            visited[row][col] = 1

            for direction in directions:
                new_row = row+direction[0]
                new_col = col+direction[1]
                
                if not self.isLand(new_row, new_col, grid):
                    perimeter += 1
                else:
                    perimeter += dfs(new_row, new_col)

            return perimeter

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return dfs(i,j)

        
        return 0

    def isLand(self, row, col, grid):
        grid_width = len(grid[0])
        grid_height = len(grid)
        return row >= 0 and row < grid_height and col >= 0 and col < grid_width and grid[row][col]
        