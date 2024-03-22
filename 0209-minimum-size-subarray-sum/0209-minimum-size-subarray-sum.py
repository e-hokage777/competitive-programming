class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        r = 0
        l = 0
        _sum = 0
        min_len = 10e6
        while r < len(nums):
            _sum+=nums[r]
            while _sum >= target:
                min_len = min(min_len, r-l+1)
                _sum-=nums[l]
                l+=1

            r+=1

        if min_len == 10e6:
            return 0
        return min_len
        