class Solution(object):
    def minSizeSubarray(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        n = len(nums)
        _sum = sum(nums)
        nums = nums + nums
        min_length = float("inf")
        for i in range(1, len(nums)):
            nums[i]+=nums[i-1]

        rem = target%_sum

        holder = {0:-1}

        if rem == 0: return n*(target//_sum)

        for i in range(len(nums)):
            diff = nums[i] - rem

            if diff in holder:
                min_length = min(min_length, i-holder[diff])

            holder[nums[i]] = i

        if min_length == float("inf"): return -1

        return min_length + n*(target//_sum)


        