class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        _min = min(0, nums[0])
        max_sum = nums[0]
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
            max_sum = max(max_sum, nums[i] - _min)

            if nums[i] < _min:
                _min = nums[i]

        return max_sum




        