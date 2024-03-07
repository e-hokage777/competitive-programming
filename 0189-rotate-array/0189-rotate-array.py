class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """


        m = k%len(nums)
        last_k = nums[-m:]
        for j in range(len(nums)-m-1, -1, -1):
            nums[(j+k)%len(nums)] = nums[j]
        
        for i, v in enumerate(last_k):
            nums[i] = v


        