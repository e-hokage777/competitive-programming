class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        holder = dict()
        count = 0
        holder[nums[0]] = 1
        if nums[0] == k: count+=1

        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
            if nums[i] == k: count += 1
            diff = nums[i] - k

            if diff in holder:
                count += holder[diff]

            holder[nums[i]] = holder.get(nums[i], 0) + 1

        return count
