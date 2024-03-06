class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        s = 0
        p = 0

        while s < len(nums):
            if(nums[s] != 0):
                nums[s], nums[p] = nums[p], nums[s]
                p += 1

            
            s += 1

        return nums
        