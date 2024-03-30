class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        count = 0
        if  nums[0]%k==0: count+=1
        
        holder = {nums[0]%k: 1}

        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
            if nums[i]%k == 0: count+=1
            if nums[i]%k in holder:
                count+=holder[nums[i]%k]

            holder[nums[i]%k] = holder.get(nums[i]%k, 0) + 1

        return count


        