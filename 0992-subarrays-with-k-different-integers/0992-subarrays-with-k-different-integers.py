class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        left_near = 0
        left_far = 0
        right = 0
        result = 0
        counter = dict()
        for right in range(len(nums)):
            counter[nums[right]] = counter.get(nums[right], 0) + 1 
            
            if len(counter) > k:
                del counter[nums[left_near]]
                left_near += 1
                left_far = left_near

            while len(counter) == k and counter[nums[left_near]] > 1:
                counter[nums[left_near]] -= 1 
                left_near += 1
            
            if len(counter) == k:result += (left_near - left_far + 1)

        return result



        