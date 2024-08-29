class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        max_num = 2**len(nums)-1
        result = []
        cur = []
        def backtrack(index, current):
            if current == max_num:
                result.append(cur[:])

            for i in range(len(nums)):
                if not current & 2**i:
                    cur.append(nums[i])
                    backtrack(index+1, current|2**i)
                    cur.pop()


        backtrack(0, 0)

        return result
        