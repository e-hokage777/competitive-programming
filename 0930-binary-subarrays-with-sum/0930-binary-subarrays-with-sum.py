class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """

        holder = dict()
        count = 0
        _sum = 0

        for i in nums:
            _sum += i

            if _sum == goal:
                count += 1

            if (_sum - goal) in holder:
                count += holder[_sum - goal]

            holder[_sum] = holder.get(_sum, 0) + 1

            
        return count