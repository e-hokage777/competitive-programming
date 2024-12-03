import math
class Solution(object):
    def maxPossibleScore(self, start, d):
        """
        :type start: List[int]
        :type d: int
        :rtype: int
        """

        self.start = start
        self.start.sort()

        min_gap = float("inf")

        for i in range(len(self.start)-1):
            min_gap = min(min_gap, self.start[i+1] - self.start[i])
        
        max_gap = min_gap + d

        ans = float("inf")

        left = min_gap
        right = max_gap + 1

        while right - left > 1:
            middle = left + (right - left)//2

            if self.check_possible(middle, d):
                left = middle
            else:
                right = middle

        return left
        
    def check_possible(self, target_diff, d):
        current_val = self.start[0]
        for i in range(len(self.start)-1):
            diff = self.start[i+1] - current_val
            if d < (target_diff - diff):
                return False
            
            current_val = self.start[i+1] + (target_diff - min(target_diff, diff))

        return True


        