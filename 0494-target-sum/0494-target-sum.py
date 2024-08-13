class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # self.count = 0

        # def dp(index, current_sum):
        #     if index == len(nums)-1:
        #         self.count += (current_sum+nums[index] == target)
        #         self.count += (current_sum-nums[index] == target)
        #         return

        #     dp(index + 1, current_sum + nums[index])
        #     dp(index + 1, current_sum - nums[index])

        # dp(0, 0)
        # return self.count

        self.count = 0
        memo = {}

        def dp(index, current_sum):
            if index == len(nums)-1:
                count = 0
                if current_sum+nums[index] == target:
                    count += 1
                if current_sum-nums[index] == target:
                    count += 1
                return count

            state = (index, current_sum)
            if state not in memo:
                memo[state] = dp(index + 1, current_sum + nums[index]) + dp(index + 1, current_sum - nums[index])

            return memo[state]

        return dp(0, 0)
        