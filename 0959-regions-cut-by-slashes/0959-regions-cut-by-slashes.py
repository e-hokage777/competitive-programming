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



class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        n = len(grid)
        tn = n*3
        transformed = [[0]*tn for _ in range(tn)]

        for i in range(n):
            for j in range(n):
                tr, tc = i*3+1, j*3+1

                if grid[i][j] == "\\":
                    transformed[tr][tc] = 1
                    transformed[tr-1][tc-1] = 1
                    transformed[tr+1][tc+1] = 1
                elif grid[i][j] == "/":
                    transformed[tr][tc] = 1
                    transformed[tr-1][tc+1] = 1
                    transformed[tr+1][tc-1] = 1

        directions = [(-1,0), (1,0), (0,1), (0,-1)]
        inbound = lambda r,c: r >= 0 and c >= 0 and r < tn and c < tn
        union_find = UnionFind(tn * tn)

        for a in transformed:
            print(a)



        for r in range(tn):
            for c in range(tn):
                index = r*tn + c

                if not transformed[r][c]:
                    for r_diff, c_diff in directions:
                        new_r, new_c = r+r_diff, c+c_diff
                        if inbound(new_r, new_c) and not transformed[new_r][new_c]:
                            new_index = new_r * tn + new_c
                            union_find.union(index, new_index)
                else:
                    union_find.parent[index] = -1

        regions = set()
        for i in range(tn):
            for j in range(tn):
                if not transformed[i][j]:
                    index = i*tn + j
                    regions.add(union_find.find(index))
                    
        return len(regions)

        


                    

        