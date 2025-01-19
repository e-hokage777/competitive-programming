from collections import deque
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def bfs(r,c):
            count = 1

            queue = deque([(r,c)])
            self.visited[r][c] = True

            while queue:
                c_r, c_c = queue.popleft()

                for dr, dc in self.directions:
                    new_r, new_c = c_r+dr, c_c+dc
                    if is_in(new_r,new_c) and not self.visited[new_r][new_c] and self.grid[new_r][new_c] == 1:
                        count += 1
                        queue.append((new_r,new_c))
                        self.visited[new_r][new_c] = True
            
            return count

            
        self.grid = grid
        self.visited = [[False]*len(grid[0]) for _ in range(len(grid))]
        self.directions = [(0,1), (0,-1), (1,0), (-1, 0)]
        is_in = lambda r,c:  r>=0 and c >= 0 and r<len(grid) and c < len(grid[0])

        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    count = bfs(r,c)
            
                    max_area = max(max_area, count)

        return max_area




        