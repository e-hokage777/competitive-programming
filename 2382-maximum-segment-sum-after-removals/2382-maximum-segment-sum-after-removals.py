from heapq import heappush

class UnionFind:
    def __init__(self, size, sums):
        self.parent = list(range(size))
        self.rank = [0] * size
        self.sums = sums
    
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def find_sum(self, x):
        x = self.find(x)
        return self.sums[x]

    def union(self, x, y):
        parentX = self.find(x)
        parentY = self.find(y)

        if parentX != parentY:
            if self.rank[parentX] > self.rank[parentY]:
                self.parent[parentY] = parentX
                self.sums[parentX] += self.sums[parentY]
            elif self.rank[parentY] > self.rank[parentX]:
                self.parent[parentX] = parentY
                self.sums[parentY] += self.sums[parentX]
            else:
                self.parent[parentY] = parentX
                self.rank[parentX] += 1
                self.sums[parentX] += self.sums[parentY]
    
class Solution(object):
    def maximumSegmentSum(self, nums, removeQueries):
        """
        :type nums: List[int]
        :type removeQueries: List[int]
        :rtype: List[int]
        """

        union_find = UnionFind(len(nums), nums)
        holder = [False] * len(nums)
        heap = []
        ans = []
        for i in range(len(removeQueries)-1, -1, -1):
            pos = removeQueries[i]

            if not heap:
                ans.append(0)
            else:
                ans.append(-heap[0])

            if pos > 0 and holder[pos-1]:
                union_find.union(pos, pos-1)
            if pos < len(removeQueries) - 1 and holder[pos+1]:
                union_find.union(pos, pos+1)

            holder[pos] = True

            heappush(heap, -union_find.find_sum(pos))


        return ans[::-1]


            
        