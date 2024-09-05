class UnionFind:
    def __init__(self, size):
        self.parent = dict([(i,i) for i in range(size)])
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
                self.parent[parentY] = parentX
            elif self.rank[parentY] > self.rank[parentX]:
                self.parent[parentX] = parentY
            else:
                self.parent[parentY] = parentX
                self.rank[parentX] += 1

    def isConnected(self, x, y):
        return self.find(x) == self.find(y)

class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """

        dsu = UnionFind(26)

        for equation in equations:
            if equation[1] == equation[2]:
                dsu.union(ord(equation[0])-97, ord(equation[-1])-97)

        for equation in equations:
            if equation[1] != equation[2] and dsu.isConnected(ord(equation[0])-97, ord(equation[-1])-97):
                return False

        return True
        