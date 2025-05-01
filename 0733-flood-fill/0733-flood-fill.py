from collections import deque
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """

        directions = [(0,1),(1,0), (0,-1), (-1, 0)]
        inbound = lambda r,c : r >= 0 and c >= 0 and r < len(image) and c < len(image[0])
        
        queue = deque([(sr, sc)])
        visited = set([(sr, sc)])
        init_color = image[sr][sc]
        image[sr][sc] = color




        while queue:
            current = queue.popleft()
            for dx, dy in directions:
                nx, ny = current[0] + dx, current[1] + dy

                if inbound(nx, ny) and image[nx][ny] == init_color and (nx, ny) not in visited:
                    image[nx][ny] = color
                    visited.add((nx, ny))
                    queue.append((nx, ny))

        return image

        