class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        switches = 0

        for num in nums:
            switches += (1<<2*num)

        for num in nums:
            if switches & (1<<2*num) and not switches & (1<<(2*num+1)):
                return num

        
        