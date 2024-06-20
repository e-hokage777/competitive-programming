class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        island_count = 0
        boolean_grid = [[False]*len(grid[0]) for _ in range(len(grid))]
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        on_land = lambda r,c: r>=0 and r<len(grid) and c>= 0 and c<len(grid[0]) and int(grid[r][c])

        def dfs(r,c):
            boolean_grid[r][c] = True

            for x,y in directions:
                new_r, new_c = r+x, c+y
                
                if not on_land(new_r, new_c): continue
                if boolean_grid[new_r][new_c]: continue

                dfs(new_r, new_c)

        count=0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if int(grid[r][c]) and not boolean_grid[r][c]:
                    count += 1
                    dfs(r,c)




        return count
        