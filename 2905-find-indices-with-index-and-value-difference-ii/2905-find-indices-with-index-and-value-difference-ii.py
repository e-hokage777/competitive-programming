class Solution(object):
    def findIndices(self, nums, indexDifference, valueDifference):
        """
        :type nums: List[int]
        :type indexDifference: int
        :type valueDifference: int
        :rtype: List[int]
        """
        if indexDifference >= len(nums):
            return [-1,-1]
        max_diff = -1
        min_diff = 1e8
        cur_min_ind = cur_max_ind = indexDifference
        for j in range(indexDifference, len(nums)):
            if nums[j] < nums[cur_min_ind]: cur_min_ind = j
            if nums[j] > nums[cur_max_ind]: cur_max_ind = j




        for i in range(len(nums) - indexDifference):
            if cur_max_ind < i+indexDifference or cur_min_ind < i+indexDifference:
                cur_min_ind = cur_max_ind = i+indexDifference
                for j in range(i+indexDifference, len(nums)):
                    if nums[j] < nums[cur_min_ind]: cur_min_ind = j
                    if nums[j] > nums[cur_max_ind]: cur_max_ind = j

            if abs(nums[i] - nums[cur_max_ind]) >= valueDifference:
                return [i, cur_max_ind]
            elif abs(nums[i] - nums[cur_min_ind]) >= valueDifference:
                return [i, cur_min_ind]



        return [-1,-1]
        