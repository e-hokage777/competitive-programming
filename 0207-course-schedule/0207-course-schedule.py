from collections import defaultdict
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        a_list = defaultdict(list)
        visited = [False]*numCourses

        for a, b in prerequisites:
            a_list[a].append(b)

        def dfs(vertex):
            
            for neighbor in a_list[vertex]:
                if neighbor in visited or not dfs(neighbor):
                    return False

            return True

        return dfs(0)
            