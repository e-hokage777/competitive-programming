class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        self.inbound = lambda x, y : x >= 0 and y >= 0 and x < len(grid) and y < len(grid[0])
        self.directions = [
            (0, 1), (1, 0), (0, -1), (-1, 0)
        ]
        self.count = 0

        self.visited = [[0] * len(grid[0]) for _ in range(len(grid))]
        self.ans= 0

        start = None
        self.target_count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    start = (i,j)

                if grid[i][j] != -1:
                    self.target_count += 1

        def recurse(position):
            curr_x, curr_y = position

            self.visited[curr_x][curr_y] = 1
            self.count += 1

            if grid[curr_x][curr_y] == 2:
                self.ans += int(self.count == self.target_count)
                self.visited[curr_x][curr_y] = 0
                self.count -= 1
                return
            for dx, dy in self.directions:
                new_x = curr_x + dx
                new_y = curr_y + dy

                if self.inbound(new_x, new_y):
                    if grid[new_x][new_y] != -1 and not self.visited[new_x][new_y]:
                        recurse((new_x, new_y))
                

            self.visited[curr_x][curr_y] = 0
            self.count -= 1
        
        recurse(start)

        return self.ans

        