class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """

        current_index = 0
        result = 0
        current_max = 0
        current_val = 1
        while current_max < n:
            while current_index < len(nums) and current_val >= nums[current_index]:
                current_max += nums[current_index]
                current_index += 1

            if current_max < current_val:
                result += 1
                current_max += current_val

            current_val = current_max+1

        return result
                

        