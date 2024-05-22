from collections import deque
class Solution(object):
    def shortestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        prefix_sum = [0]
        min_len = float("inf")
        for i in range(len(nums)):
            prefix_sum.append(nums[i] + prefix_sum[-1])

        monotonic_stack = []

        for index, number in enumerate(prefix_sum):

            ## ensuring stack is monotonic
            while monotonic_stack and monotonic_stack[-1][1] > number:
                monotonic_stack.pop()

            ## binary search over monotonic_stack(sorted by default)
            at_least = number - k
            left = 0
            right = len(monotonic_stack) - 1

            while left <= right:
                middle = left + (right - left)//2

                if monotonic_stack[middle][1] <= at_least:
                    min_len = min(min_len, index - monotonic_stack[middle][0])
                    left = middle+1
                else:
                    right = middle - 1

            monotonic_stack.append([index, number])

        return -1 if min_len == float("inf") else min_len