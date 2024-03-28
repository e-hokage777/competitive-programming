class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_ind = 0
        _min = 0
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
            if nums[i] > nums[max_ind]:
                max_ind = i

        for i in range(max_ind):
            if nums[i] < _min:
                _min = nums[i]

        return nums[max_ind] - _min

        