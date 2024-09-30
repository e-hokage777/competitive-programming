class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        i = len(nums)-1
        j = len(nums)-1

        for i in range(len(nums)):
            j = len(nums)-1
            while j > i:
                if self.compare(nums[j], nums[j-1]):
                    nums[j],nums[j-1] = nums[j-1], nums[j]
                j-=1

        return "".join([str(x) for x in nums])

    def compare(self,a,b):
        if "".join([str(a),str(b)]) > "".join([str(b),str(a)]): return True
        return False
                

        
        