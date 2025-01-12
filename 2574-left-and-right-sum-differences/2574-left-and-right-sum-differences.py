class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        prefix_left = [0]
        prefix_right = [0]

        for i in range(len(nums)):
            prefix_left.append(prefix_left[-1] + nums[i])
            prefix_right.append(prefix_right[-1] + nums[-i-1])

        ans = []
        for i in range(len(nums)):
            ans.append(abs(prefix_left[i]-prefix_right[-i-2]))

        return ans