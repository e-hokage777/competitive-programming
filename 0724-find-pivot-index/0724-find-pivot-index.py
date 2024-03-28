class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left_sum = 0
        right_sum = sum(nums[1:])
        l = 0

        while l < len(nums)-1 and left_sum < right_sum:

            left_sum+=nums[l]
            right_sum-=nums[l+1]
            l+=1


        if left_sum == right_sum:
            return l
        else:
            return -1
        