class Solution(object):
    def goodIndices(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        

        left = [0]
        right = [0]

        inc_count = 0
        dec_count = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                inc_count += 1
            else:
                inc_count = 0

            if nums[-i] >= nums[-i-1]:
                dec_count += 1
            else:
                dec_count = 0

            left.append(inc_count)
            right.append(dec_count)

        right = right[::-1]


        ans = []
        for i in range(k, len(nums)-k):
            if left[i-1]+1 >= k and right[i+1]+1 >= k:
                ans.append(i)
        
        return ans


        