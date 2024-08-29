class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []
        cur = []
        self.visited = 0

        def backtrack(index):
            if index >= len(nums):
                result.append(cur[:])

            for i in range(len(nums)):
                if not (1<<i) & self.visited:
                    self.visited |= (1<<i)
                    cur.append(nums[i])
                    backtrack(index+1)
                    self.visited ^= (1<<i)
                    cur.pop()


        backtrack(0)

        return result
        