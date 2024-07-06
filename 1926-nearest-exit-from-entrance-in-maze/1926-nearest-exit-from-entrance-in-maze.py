from collections import deque
class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """

        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        isboundary = lambda r,c: r == 0 or c == 0 or r == len(maze)-1 or c == len(maze[0])-1
        inbound = lambda r, c: r >= 0 and c >= 0 and r < len(maze) and c < len(maze[0])

        queue = deque([tuple(entrance)])
        visited = set([tuple(entrance)])

        steps = 0

        while queue:
            length = len(queue)
            steps+=1
            for _ in range(length):
                curr_r, curr_c = queue.popleft()

                for x,y in directions:
                    new_r, new_c = curr_r + x, curr_c + y
                    if not inbound(new_r,new_c) or (new_r, new_c) in visited or maze[new_r][new_c] != ".": continue
                    if isboundary(new_r, new_c):return steps
                    visited.add((new_r, new_c))
                    queue.append((new_r,new_c))

        return -1




        