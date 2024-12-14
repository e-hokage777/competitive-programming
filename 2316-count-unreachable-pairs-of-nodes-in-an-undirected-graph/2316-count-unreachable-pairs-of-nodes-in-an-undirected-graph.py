from collections import defaultdict

class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size
    
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]

        return x

    def union(self, x, y):
        parentX = self.find(x)
        parentY = self.find(y)

        if parentX != parentY:
            if self.rank[parentX] > self.rank[parentY]:
                self.parent[parentX] = parentY
            elif self.rank[parentY] > self.rank[parentX]:
                self.parent[parentY] = parentX
            else:
                self.parent[parentY] = parentX
                self.rank[parentX] += 1


class Solution(object):
    def countPairs(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """

        union_find = UnionFind(n)

        ## forming groups of nodes for which path exists
        for a, b in edges:
            union_find.union(a,b)
        
        components = defaultdict(int)

        ## finding number of elements in each component
        for i in range(n):
            parent = union_find.find(i)
            components[parent] += 1

        group_sizes = list(components.values())

        ## cummulative sum of group sizes while traversing array
        cum_group_size = 0
        ans = 0

        for size in group_sizes:
            ans += (size * cum_group_size)
            cum_group_size += size

        return ans


        