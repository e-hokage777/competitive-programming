class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        def dp(i, last):
            if i >= len(nums): return 0

            state = (i, last)
            if state not in memo:
                include = 0
                if last < nums[i]:
                    include = 1 + dp(i+1, nums[i])
                
                exclude = dp(i+1, last)

                memo[(i, last)] = max(include, exclude)

            return memo[state]

        memo = {}

        return dp(0,-20000)

        