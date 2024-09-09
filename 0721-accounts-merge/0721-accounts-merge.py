from collections import defaultdict
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
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        unionFind = UnionFind(len(accounts))
        mappings = dict()
        for i in range(len(accounts)):
            for email in accounts[i][1:]:
                if email in mappings:
                    unionFind.union(i,mappings[email])
                else:
                    mappings[email] = i

        result = []

        merged_accounts = defaultdict(set)
        for account_idx,parent_idx in unionFind.parent.items():
            for email in accounts[account_idx][1:]:
                merged_accounts[parent_idx].add(email)

        for account_idx in merged_accounts:
            result.append([accounts[account_idx][0]] + sorted(list(sorted(merged_accounts[account_idx]))))

        return result