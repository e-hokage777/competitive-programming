class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = len(nums)
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = float("inf")
                k -= 1

        nums.sort()

        return k
        

        