class UnionFind:
    def __init__(self, size):
        self.parent = dict([(i,i) for i in range(size)])
        self.rank = [0] * size

    def find(self, x):
        while x != self.parent[x]:
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
        
class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        row_reps = dict()
        col_reps = dict()
        union_find = UnionFind(len(stones))
        
        for i, (r,c) in enumerate(stones):
            if r in row_reps:
                union_find.union(i, row_reps[r])
            else:
                row_reps[r] = i
            if c in col_reps:
                union_find.union(i, col_reps[c])
            else:
                col_reps[c] = i


        return len(stones) - len(set([union_find.find(i) for i in range(len(stones))]))
