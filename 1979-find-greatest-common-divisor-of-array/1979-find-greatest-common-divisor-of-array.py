class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def gcd(a,b):
            if b == 0: return a
            return gcd(b, a%b)

        largest = nums[0]
        smallest = nums[0]

        for num in nums:
            if num > largest: largest = num
            if num < smallest: smallest = num

        return gcd(largest, smallest)
        