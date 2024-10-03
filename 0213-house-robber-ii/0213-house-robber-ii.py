class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if(len(nums) == 1):
            return nums[0]

        def dp(index, last_robbed, first_robbed):
            if (first_robbed and index == len(nums)-1) or index >= len(nums):
                # print(first_robbed, index,"here")
                return 0

            state = (index, last_robbed, first_robbed)

            if state not in memo:
                if not last_robbed:
                    memo[state] = max(nums[index] + dp(index+1, True, first_robbed), dp(index+1,False,first_robbed))
                else:
                    memo[state] = dp(index+1,False,first_robbed)
                
            return memo[state]

        memo = dict()


        return max(dp(1, False, False), dp(0, False, True))

        