import bisect
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()
        ans = sum(nums[:3])
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                remainder = target - (nums[i] + nums[j])
                index_found = bisect_left(nums, remainder, lo=j+1)
                index_found = min(len(nums)-1, index_found)
                if index_found + 1 < len(nums):
                    if abs(remainder - nums[index_found+1]) < abs(remainder-nums[index_found]):
                        index_found = index_found + 1

                _sum = nums[i] + nums[j] + nums[index_found]

                if abs(target - _sum) < abs(target - ans):
                    ans = _sum

        return ans
