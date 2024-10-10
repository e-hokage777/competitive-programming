class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        duplicates = set()

        for i in range(len(nums)):
            while nums[i] != i+1:
                temp = nums[i] - 1
                if nums[temp] == nums[i]:
                    duplicates.add(nums[i])
                    break

                nums[i], nums[temp] = nums[temp], nums[i]

        return duplicates

        
        