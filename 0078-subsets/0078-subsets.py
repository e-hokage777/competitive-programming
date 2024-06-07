class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        self.subset = []
        self.result = [[]]

        def backtrack(index):
            if index >= len(nums):
                return

            for i in range(index, len(nums)):
                self.subset.append(nums[i])
                backtrack(i+1)
                # print(self.subset)
                self.result.append(self.subset[:])
                self.subset.pop()

        backtrack(0)

        return self.result

        



        