
from collections import deque
class Solution(object):
    def continuousSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        inc_stack = deque([])
        dec_stack = deque([])
        count = 0

        l = 0
        for r in range(len(nums)):
            while inc_stack and inc_stack[-1] > nums[r]:
                inc_stack.pop()
            inc_stack.append(nums[r])

            while dec_stack and dec_stack[-1] < nums[r]:
                dec_stack.pop()
            dec_stack.append(nums[r])

            while abs(inc_stack[0] - dec_stack[0]) > 2:
                print("here")
                if nums[l] == inc_stack[0]:
                    inc_stack.popleft()

                if nums[l] == dec_stack[0]:
                    dec_stack.popleft()

                l += 1

            count += (r-l)+1

        return count
        