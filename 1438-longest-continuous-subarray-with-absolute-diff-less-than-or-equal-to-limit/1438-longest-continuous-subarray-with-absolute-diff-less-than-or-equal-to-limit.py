from collections import deque
class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """

        r = 0
        queue = deque()
        max_len = 0
        while r < len(nums):
            queue.append(nums[r])
            while len(queue) > 0 and abs(queue[0] - queue[-1]) > limit:
                queue.popleft()

            max_len = max(max_len, len(queue))
            r+=1

        return max(max_len, len(queue))
            



        