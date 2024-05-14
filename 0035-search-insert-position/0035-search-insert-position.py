class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left = 0
        right = len(nums)-1

        while left <= right:
            middle = left + (right - left)//2
            if nums[middle] == target:
                return middle
            elif target > nums[middle]:
                left = middle + 1
            else:
                right = middle - 1

        if target > nums[middle]:
            return middle + 1
        
        return max(0, middle)