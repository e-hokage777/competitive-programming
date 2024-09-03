class UnionFind:
    def __init__(self, size):
        self.parent = dict([(i,i) for i in range(size)])
        self.rank = [0] * size

    def find(self,x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]

        return x

    def union(self, x, y):
        parentX = self.find(x)
        parentY = self.find(y)

        if parentX != parentY:
            if self.rank[parentX] > self.rank[parentY]:
                self.parent[parentY] = parentX
            elif self.rank[parentY] > self.rank[parentX]:
                self.parent[parentX] = parentY
            else:
                self.parent[parentY] = parentX
                self.rank[parentX] += 1

    def isConnected(self, x, y):
        return self.find(x) == self.find(y)

class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """

        n = len(isConnected)
        dsu = UnionFind(n)
        components = n

        for i in range(n):
            for j in range(i, n):
                if isConnected[i][j] and not dsu.isConnected(i,j):
                    dsu.union(i,j)
                    components -= 1

        return components


        