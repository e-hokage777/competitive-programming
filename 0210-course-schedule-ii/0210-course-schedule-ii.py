from collections import defaultdict
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        order = []
        parent_count = [0]*numCourses
        adj_list = defaultdict(list)
        for course, pre in prerequisites:
            adj_list[course].append(pre)
            parent_count[pre] += 1

        queue = deque()

        for i in range(numCourses):
            if not parent_count[i]:
                queue.append(i)

        while queue:
            current_course = queue.popleft()
            order.append(current_course)

            for i in adj_list[current_course]:
                parent_count[i] -= 1
                
                if not parent_count[i]:
                    queue.append(i)

        
        return order[::-1] if len(order) == numCourses else []

        