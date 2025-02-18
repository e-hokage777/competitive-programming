from bisect import bisect_right
class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        
        ## binary search is probably the right answer
        ## (got this idea while thinking of similar patterns)
        
        self.positions = sorted(position)
        self.m = m
        
        left = 1
        right = self.positions[-1]


        while right - left > 1:
            middle = left + (right - left)//2

            if self.test(middle):
                left = middle
            else:
                right = middle - 1

        if self.test(right):
            return right
        
        return left

    def test(self, dist):
        prev_pos = self.positions[0]
        m = self.m - 1
        for i in range(1, len(self.positions)):
            if self.positions[i] - prev_pos >= dist:
                prev_pos = self.positions[i]
                m -= 1
            
            if not m:
                break

        return True if m <= 0 else False
