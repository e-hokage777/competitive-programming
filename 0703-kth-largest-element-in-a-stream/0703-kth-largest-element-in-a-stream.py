from heapq import *
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.nums = sorted(nums)[-k:]
        self.k = k

        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.nums) >= self.k:
            heappushpop(self.nums, val)
        else:
            heappush(self.nums, val)
        return nlargest(self.k, self.nums)[-1]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)