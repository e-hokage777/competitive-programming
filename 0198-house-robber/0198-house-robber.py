class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = {}
        def dp(i):
            if i >= len(nums):
                return 0

            state = i
            if state not in memo:
                include = nums[i] + dp(i+2)
                exclude = dp(i+1)

                memo[state] = max(include, exclude)

            return memo[state]

        return dp(0)
        