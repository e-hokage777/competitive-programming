class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        non_zeros = []
        zeros = []
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i]*=2
                nums[i+1] = 0

            if nums[i] == 0:
                zeros.append(nums[i])
            else: non_zeros.append(nums[i])

        if nums[-1] == 0:
            zeros.append(nums[-1])
        else: non_zeros.append(nums[-1])

        return non_zeros + zeros
            
        