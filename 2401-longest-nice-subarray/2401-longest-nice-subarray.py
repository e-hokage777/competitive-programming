class Solution(object):
    def longestNiceSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_length = 1
        for i in range(len(nums)):
            holder = nums[i]
            length = 1
            for j in range(i+1, min(i+30, len(nums))):
                if holder & nums[j]:
                    break
                
                holder |= nums[j]

                length += 1
                max_length = max(length, max_length)

        return max_length
                
                
                    
