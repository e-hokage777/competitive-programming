from collections import deque
from collections import deque
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """


        inbound = lambda x,y: 0<=x<len(mat) and 0<=y<len(mat[0])

        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        visited = [[-1]*len(mat[0]) for _ in range(len(mat))]

        queue = deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append((i,j))
                    visited[i][j] = 0


        while queue:
            curr_x, curr_y = queue.popleft()

            for x,y in directions:
                new_r, new_c = curr_x + x, curr_y + y
                if not inbound(new_r, new_c) or visited[new_r][new_c] >= 0: continue

                visited[new_r][new_c] = visited[curr_x][curr_y] + 1
                queue.append((new_r, new_c))

        return visited





        
        