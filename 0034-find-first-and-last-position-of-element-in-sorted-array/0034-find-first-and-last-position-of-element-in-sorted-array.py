class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        if len(nums) == 0:
            return [-1,-1]
        min_ind = self.findBoundIndex(nums, target)

        if min_ind == -1:
            return [-1, -1]
        else:
            return [min_ind, self.findBoundIndex(nums, target, False)]

    def findBoundIndex(self, nums, target, _min = True):
        l = 0
        r = len(nums)  - 1

        while l <= r:
            mid = l + (r-l)//2

            if nums[mid] == target:
                if _min:
                    r = mid - 1
                else:
                    l = mid + 1
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        if _min:
            print(l)
            return l  if l<= len(nums)-1 and nums[l] == target else -1
        return r if r  >= 0 and nums[r] == target else -1
