class Solution(object):
    def resultsArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        left = 0
        right = 0
        results = []

        for left in range(len(nums) - k + 1):
            while right - left + 1 < k and nums[right] - nums[left] == right - left:
                right += 1

            if right - left + 1 == k and nums[right] - nums[left] == right - left:
                results.append(nums[right])
                right += 1
            else:
                results.append(-1)

        return results

        

        

        