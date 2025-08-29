from collections import deque, defaultdict

class Solution(object):
    def sortItems(self, n, m, group, beforeItems):
        """
        :type n: int
        :type m: int
        :type group: List[int]
        :type beforeItems: List[List[int]]
        :rtype: List[int]
        """

        ## topological sort items
        ## topological sort groups
        ## move through topological sort of groups and add items into an answer array

        ## assigning groups to items without groups
        last_group_index = max(group) + 1

        for i, group_index in enumerate(group):
            if group_index == -1:
                group[i] = last_group_index
                last_group_index += 1

        ## topological sort 
        items_indegree = [0] * len(beforeItems) 
        groups_indegree = [0] * (last_group_index)
        items_graph = defaultdict(list)
        groups_graph = defaultdict(list)


        for i in range(len(beforeItems)):
            current_item_group = group[i]
            for item in beforeItems[i]:
                items_graph[item].append(i)
                items_indegree[i] += 1

                before_group = group[item]

                if current_item_group != before_group:
                    groups_graph[before_group].append(current_item_group)
                    groups_indegree[current_item_group] += 1

        ## topological sort items
        sorted_items = []
        queue = deque()
        for item in range(n):
            if items_indegree[item] == 0:
                queue.append(item)

        while queue:
            current = queue.popleft()
            sorted_items.append(current)

            for child in items_graph[current]:
                items_indegree[child] -= 1

                if items_indegree[child] == 0:
                    queue.append(child)

        groups_map = defaultdict(list)

        for item in sorted_items:
            groups_map[group[item]].append(item)
        

        
        queue = deque()

        for group_item in range(last_group_index):
            if groups_indegree[group_item] == 0:
                queue.append(group_item)


        result = []

        print(groups_graph)
        visited = [False] * n
        while queue:
            current = queue.popleft()
            result += groups_map[current]

            visited[current] = True

            for child in groups_graph[current]:
                groups_indegree[child] -= 1
                
                if groups_indegree[child] == 0:
                    queue.append(child)

        
        return result if len(result) == n else []
            



        