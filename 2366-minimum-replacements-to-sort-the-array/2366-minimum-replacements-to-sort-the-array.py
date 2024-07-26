class Solution(object):
    def minimumReplacement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        num_ops = 0
        for i in range(len(nums)-1 , 0, -1):
            if nums[i] < nums[i-1]:
                remainder = nums[i-1]%nums[i]
                if remainder == 0:
                    num_ops += nums[i-1]//nums[i] - 1
                    nums[i-1] = nums[i]
                else:
                    num_ops += nums[i-1]//nums[i]
                    nums[i-1] = remainder 

        return num_ops
        