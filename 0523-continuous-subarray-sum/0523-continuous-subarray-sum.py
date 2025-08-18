class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        if len(nums) < 2:
            return False

        prefix_sum = [nums[0]]


        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])

        index_map = dict()

        print(prefix_sum)

        for i in range(len(prefix_sum)):

            val = prefix_sum[i]
            mod = val % k
            
            if i > 0 and (val == 0 or mod == 0):
                return True

            if mod not in index_map:
                index_map[mod] = i
            else:
                if index_map[mod] + 1 < i:
                    return True
        

        return False

            


        