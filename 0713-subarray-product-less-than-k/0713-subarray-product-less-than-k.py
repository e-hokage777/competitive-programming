class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        if k <= 1:
            return 0

        l=0
        r=0
        pdt=1
        count = 0
        while r < len(nums):
            pdt*=nums[r]
            while pdt>=k:
                pdt//=nums[l]
                l+=1

            count+= (r-l+1)
            r+=1


        return count


        