from collections import deque
class Solution(object):
    def highestPeak(self, isWater):
        """
        :type isWater: List[List[int]]
        :rtype: List[List[int]]
        """
        
        directions = [(1,0),(-1,0),(0,-1),(0,1)]
        inbound = lambda r,c : r>=0 and c>=0 and r < len(isWater) and c < len(isWater[0])
        visited = [[False]*len(isWater[0]) for _ in range(len(isWater))]


        queue = deque()
        for i in range(len(isWater)):
            for j in range(len(isWater[0])):
                if isWater[i][j]:
                    visited[i][j] = True
                    queue.append((i,j))
                    isWater[i][j]=0
                


        while queue:
            curr_r, curr_c = queue.popleft()
            
            for x,y in directions:
                new_r, new_c = curr_r+x, curr_c+y
                if not inbound(new_r, new_c) or visited[new_r][new_c]: continue
                visited[new_r][new_c] = True
                height = isWater[curr_r][curr_c] + 1
                isWater[new_r][new_c] = height
                queue.append((new_r, new_c))
        return isWater

        