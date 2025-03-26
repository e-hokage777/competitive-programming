
class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """

        ## approach 1:  binary search to find number closest to each number
        ## approach 2: add all arrays and mark them by list they come from and the 2-pointers

        full_list = []
        k = len(nums)

        if len(nums) == 1:
            return [nums[0][0], nums[0][0]]

        for i in range(len(nums)):
            for val in nums[i]:
                full_list.append((val, i))

        full_list.sort()

        left = 0
        right = 0

        counter = dict()
        min_range = float("inf")
        ans = [-1, -1]



        for right in range(len(full_list)):
            counter[full_list[right][1]] = counter.get(full_list[right][1], 0) + 1
            while left < right and len(counter) >= k:
                current_range = full_list[right][0] - full_list[left][0]
                if current_range < min_range:
                    min_range = current_range
                    ans = [full_list[left][0], full_list[right][0]]
                
                if counter[full_list[left][1]] == 1:
                    del counter[full_list[left][1]]
                else:
                    counter[full_list[left][1]] -= 1

                left += 1


        
        return ans
            



        