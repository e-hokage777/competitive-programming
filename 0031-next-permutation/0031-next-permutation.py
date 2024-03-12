class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        if len(nums) <= 1:
            return

        swap_idx = len(nums)
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                swap_idx = i-1
                break

        if swap_idx == len(nums):
            nums.sort()
            return


        replace_idx = len(nums)-1
        for j in range(swap_idx+1, len(nums)):
            if nums[j] <= nums[swap_idx]:
                replace_idx = j-1
                break



        nums[swap_idx], nums[replace_idx] = nums[replace_idx], nums[swap_idx]

        for m in range(swap_idx+1, len(nums)-1):
            for n in range(m+1, len(nums)):
                if nums[n] < nums[m]:
                    nums[m], nums[n] = nums[n], nums[m]