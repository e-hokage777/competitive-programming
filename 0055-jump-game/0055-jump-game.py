class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        def dfs(index):
            if index >= len(nums)-1: return True
            if nums[index] == 0: return False

            for i in range(1,nums[index]+1):
                new_index = i + index
                if dfs(new_index): return True
            
            return False

        return dfs(0)
        