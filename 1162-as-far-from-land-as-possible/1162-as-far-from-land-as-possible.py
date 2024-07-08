from collections import deque
class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        inbound = lambda r,c: r>=0 and c>=0 and r < len(grid) and c < len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        max_distance = -1

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if not grid[i][j]:
                    found=False

                    queue = deque([(i,j)])
                    visited = set([(i,j)])

                    while queue:
                        for _ in range(len(queue)):
                            curr_r,curr_c = queue.popleft()

                            for x,y in directions:
                                new_r, new_c = curr_r+x, curr_c+y
                                if not inbound(new_r,new_c) or (new_r,new_c) in visited: continue
                                if grid[new_r][new_c]:
                                    max_distance = max((abs(i-new_r) + abs(j-new_c)), max_distance)
                                    found = True
                                    break
                                visited.add((new_r, new_c))
                                queue.append((new_r,new_c))

                            if found: break
                        if found: break

        return max_distance





        