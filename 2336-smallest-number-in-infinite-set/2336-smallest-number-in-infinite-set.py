from heapq import heappush, heappop
class SmallestInfiniteSet(object):

    def __init__(self):
        self.heap = []
        self.current = 1
        self.added_back = set()

    def popSmallest(self):
        """
        :rtype: int
        """

        if self.heap and self.heap[0] < self.current:
            smallest = heappop(self.heap)
            self.added_back.remove(smallest)
            return smallest
        else:
            smallest = self.current
            self.current += 1
            return smallest
        

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """

        if num < self.current and num not in self.added_back:
            heappush(self.heap, num)
            self.added_back.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)