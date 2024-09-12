class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        ## first xor to find a^b where a and b are the numbers that occur once
        a_x_b = 0
        for num in nums:
            a_x_b ^= num

        ## finding first spot where they differ
        comparator = 1
        while not comparator & a_x_b:
            comparator <<= 1

        ## grouping into those that have 1 at that spot and those that have 0
        ones = 0
        zeros = 0
        for num in nums:
            if comparator & num:
                ones^=num
            else:
                zeros^=num

        return [a_x_b^ones, a_x_b^zeros]
        