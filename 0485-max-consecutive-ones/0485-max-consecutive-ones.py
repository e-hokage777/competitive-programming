class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count = 0
        current_count = 0

        for num in nums:
            if num == 0:
                if current_count > max_count:
                    max_count = current_count
                
                current_count = 0

            else:
                current_count += 1

        if current_count > max_count:
            max_count = current_count


        return max_count
        