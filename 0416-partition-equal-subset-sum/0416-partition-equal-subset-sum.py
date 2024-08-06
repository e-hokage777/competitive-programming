class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        def dp(i, target_sum):
            if i >= len(nums) or target_sum == 0:
                return target_sum == 0

            return dp(i+1, target_sum) or dp(i+1, target_sum-nums[i])
        
        _sum = sum(nums)
        
        return _sum%2==0 and dp(0, _sum//2)