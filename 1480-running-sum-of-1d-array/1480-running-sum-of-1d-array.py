class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        _sum = 0
        result = []
        for i in range(len(nums)):
            _sum+=nums[i]
            result.append(_sum)

        return result

        