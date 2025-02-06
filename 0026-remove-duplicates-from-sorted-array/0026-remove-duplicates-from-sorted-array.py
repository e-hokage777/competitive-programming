class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        found = set()

        for i in range(len(nums)):
            if nums[i] in found:
                nums[i] = "_"
            else:
                found.add(nums[i])
        
        for i in range(1, len(nums)):
            j = i
            while j > 0 and nums[j-1] == "_":
                nums[j], nums[j-1] = nums[j-1], nums[j]
                j-=1

        print(nums)

        return len(found)
        