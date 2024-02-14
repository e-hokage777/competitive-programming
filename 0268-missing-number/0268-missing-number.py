class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        print(nums)

        for i in range(len(nums)):
            if i != nums[i]:
                return i

        return i+1
        