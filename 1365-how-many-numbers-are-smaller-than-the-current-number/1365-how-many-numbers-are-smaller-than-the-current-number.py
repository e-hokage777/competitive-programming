class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        less_count = dict()
        sorted_nums = sorted(nums, reverse=True)
        current_num = sorted_nums[0]

        for i in range(len(nums)):
            if sorted_nums[i] != current_num:
                less_count[current_num] = len(sorted_nums)-i
                current_num = sorted_nums[i]

        return [less_count.get(i,0) for i in nums]
        