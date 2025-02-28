class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        for i in range(1, len(nums)):
            nums[i] = (nums[i] + nums[i-1])

        nums.append(0)        
        nums.sort()

        return nums[-1] - nums[0]