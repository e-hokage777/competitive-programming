class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        stack = []
        curr_min = nums[0]

        for n in nums:
            while stack and n >= stack[-1][0]:
                stack.pop()

            if stack and n > stack[-1][1]:
                return True

            curr_min = min(curr_min, n)
            stack.append([n, curr_min])

        return False