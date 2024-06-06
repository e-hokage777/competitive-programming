from itertools import permutations

class Solution(object):
    def distributeCookies(self, cookies, k):
        """
        :type cookies: List[int]
        :type k: int
        :rtype: int
        """

        kids = [0]*k
        self.min_unfairness = float("inf")
        def backtrack(index):
            if index >= len(cookies):
                unfairness = max(kids)
                self.min_unfairness = min(self.min_unfairness, unfairness)
                return

            for i in range(k):
                kids[i] += cookies[index]
                if kids[i] > self.min_unfairness:
                    kids[i] -= cookies[index]
                    continue
                backtrack(index + 1)
                kids[i] -= cookies[index]

        backtrack(0)

        return self.min_unfairness