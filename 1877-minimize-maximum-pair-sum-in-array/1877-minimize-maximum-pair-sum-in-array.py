class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        max_pair_sum = 0
        for i in range(len(nums)//2):
            if nums[i] + nums[len(nums)-i-1] > max_pair_sum:
                max_pair_sum = nums[i] + nums[len(nums)-i-1]

        return max_pair_sum
