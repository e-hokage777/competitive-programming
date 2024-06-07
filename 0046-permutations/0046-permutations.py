class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        self.result = set()
        def backtrack(index):
            if index >= len(nums):
                return

            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                backtrack(index+1)
                self.result.add(tuple(nums[:]))
                nums[i], nums[index] = nums[index], nums[i]


        backtrack(0)

        return list(self.result)
        