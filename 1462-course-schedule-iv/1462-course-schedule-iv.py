class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        
        grid = [[False]*numCourses for _ in range(numCourses)]


        for u, v in prerequisites:
            grid[u][v] = True

        for i in range(numCourses):
            for r in range(numCourses):
                for c in range(numCourses):
                    if grid[r][i] and grid[i][c]:
                        grid[r][c] = True

        ans = []
        for a,b in queries:
            ans.append(grid[a][b])

        return ans
