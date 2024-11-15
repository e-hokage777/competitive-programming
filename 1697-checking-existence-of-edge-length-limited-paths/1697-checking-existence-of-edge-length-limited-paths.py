class UnionFind():
    def __init__(self, size):
        self.parent= [i for i in range(size)]
        self.rank = [0] * size

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        
        return x
    
    def union(self, x, y):
        parentX = self.find(x)
        parentY = self.find(y)

        if parentX == parentY:
            return
        elif self.rank[parentX] > self.rank[parentY]:
            self.parent[parentY] = parentX
        elif self.rank[parentY] > self.rank[parentX]:
            self.parent[parentX] = parentY
        else:
            self.parent[parentY] = parentX
        
    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution(object):
    def distanceLimitedPathsExist(self, n, edgeList, queries):
        """
        :type n: int
        :type edgeList: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """

        edgeList = sorted(edgeList, key=lambda x: x[-1])
        queries = [[q[0], q[1], q[2], i] for i,q in enumerate(queries)]
        queries = sorted(queries, key=lambda x: x[-2])

        union_find = UnionFind(n)
        current_edge = 0
        holder = []
        for query in queries:
            while current_edge < len(edgeList) and edgeList[current_edge][-1] < query[-2]:
                union_find.union(edgeList[current_edge][0], edgeList[current_edge][1])
                current_edge += 1
            
            if union_find.connected(query[0], query[1]):
                holder.append((query[-1], True))
            else:
                holder.append((query[-1], False))


        ans = [False] * len(queries)

        for index, value in holder:
            ans[index] = value

        return ans


        