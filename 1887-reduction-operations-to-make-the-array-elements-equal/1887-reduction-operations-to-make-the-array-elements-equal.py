class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count = 0
        nums.sort(reverse = True)
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                count+=i+1
        
        return count


        