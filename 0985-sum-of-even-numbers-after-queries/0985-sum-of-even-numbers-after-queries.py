class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """

        sum_evens = 0
        ans = []

        for num in nums:
            if not num%2:
                sum_evens += num

        
        for val, index in queries:
            old_val = nums[index]
            new_val = nums[index] + val

            if not new_val % 2:
                if not old_val % 2:
                    sum_evens += (new_val - old_val)
                else:
                    sum_evens += new_val

            ans.append(sum_evens)
                
            nums[index] = new_val


        return ans
        