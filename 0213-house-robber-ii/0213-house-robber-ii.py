class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if(len(nums) == 1): return nums[0]

        start_first_grid = [[0]*(len(nums)+1) for _ in range(2)]
        start_second_grid = [[0]*(len(nums)+1) for _ in range(2)]

        for i in range(2,len(nums)+1):
            index = i-1
            start_second_grid[0][i] = nums[index] + max(start_second_grid[1][:i])
            start_second_grid[1][i] = max(start_second_grid[0][:i])

        for i in range(1,len(nums)):
            index = i-1
            start_first_grid[0][i] = nums[index] + max(start_first_grid[1][0:i])
            start_first_grid[1][i] = max(start_first_grid[0][0:i])

        max1 = max(start_first_grid[0][-2], start_first_grid[1][-2])
        max2 = max(start_second_grid[0][-1], start_second_grid[1][-1])

        # print(start_first_grid, start_second_grid)

        return max(max1, max2)





        