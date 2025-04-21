from collections import defaultdict

class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """

        prefix_sum = []
        prefix_sum.append(nums[0])
        counter = {prefix_sum[0]: 0}

        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])
            if prefix_sum[-1] not in counter:
                counter[prefix_sum[-1]] = i

        
        ans = float("inf")
        right_side = 0


        for i in range(len(nums)-1, -1, -1):
            remainder = x - right_side

            if counter.get(remainder, float("inf")) < i:
                potential = len(nums) - i + counter[remainder]
                ans = min(potential, ans)

            right_side += nums[i]

            if right_side == x:
                ans = min(ans, len(nums) - i)

        return ans if ans != float("inf")  else -1


        
        