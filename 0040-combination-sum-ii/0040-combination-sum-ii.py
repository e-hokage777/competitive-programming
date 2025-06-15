class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.candidates = sorted(candidates)
        self.ans = set()
        arr = []
        def recurse(index):
            _sum = sum(arr)
            if _sum > target:
                return

            if index == len(self.candidates):
                if _sum == target:
                    self.ans.add(tuple(arr))
                return

            arr.append(self.candidates[index])
            recurse(index + 1)
            arr.pop()
            recurse(index + 1)

        recurse(0)

        return list(map(list, self.ans))

        