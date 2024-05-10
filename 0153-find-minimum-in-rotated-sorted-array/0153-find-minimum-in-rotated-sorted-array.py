class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        l = 0
        r = len(nums) - 1
        min_mid = float("inf")
        while l < r:
            mid = l + (r-l)//2
            min_mid = min(min_mid, nums[mid])
            if nums[mid] < nums[l] and nums[mid] < nums[r]:
                if nums[l] > nums[r]: r = mid-1
                else: l = mid+1
            elif nums[mid] > nums[l] and nums[mid] > nums[r]:
                if nums[l] < nums[r]: r = mid-1
                else: l = mid+1
            else:
                if nums[l] < nums[r]: r = mid-1
                else: l = mid+1

        
        return min(nums[l], min_mid)

        # while l <= r:
        #     mid = l + (r-l)//2

        #     if (mid == 0 and nums[mid] < nums[mid+1]) or\
        #     (mid == len(nums)-1 and nums[mid] < nums[mid-1]) or\
        #     (nums[mid] < nums[mid-1] and nums[mid] < nums[mid+1]):
        #         return nums[mid]
        #     elif nums[mid] > nums[mid-1]: l = mid + 1
        #     else: r = mid - 1

        # return -1
