class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones = 0
        twos = 0

        for num in nums:
            twos ^= (ones & num)
            ones ^= num

            ones, twos = ~(ones & twos) & ones, ~(ones & twos) & twos
            
        return ones
        
        