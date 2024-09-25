from heapq import heappush, heappop
class MedianFinder(object):

    def __init__(self):
        self.left_heap = []
        self.right_heap = []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # if not self.left_heap and not self.right_heap:
        #     heappush(self.left_heap, -num)
        # elif self.left_heap and not self.right_heap:
            
        #     if -self.left_heap[0] > num:
        #         heappush(self.right_heap, -heappop(self.left_heap))
        #         heappush(self.left_heap, -num)
        #     else:
        #         heappush(self.right_heap, num)

        # else:
        #     if num >  -self.left_heap[0]:
        #         heappush(self.right_heap,num)
        #     else:
        #         heappush(self.left_heap, -num)

        # if len(self.right_heap) > len(self.left_heap):
        #     heappush(self.left_heap, -heappop(self.right_heap))
        
        # if len(self.left_heap) - len(self.right_heap) > 1:
        #     heappush(self.right_heap, -heappop(self.left_heap))

        heappush(self.left_heap, -num)

        if len(self.left_heap) - len(self.right_heap) > 1:
            heappush(self.right_heap, -heappop(self.left_heap))

        if self.right_heap and -self.left_heap[0] > self.right_heap[0]:
            heappush(self.right_heap, -heappop(self.left_heap))

        if len(self.right_heap) > len(self.left_heap):
            heappush(self.left_heap, -heappop(self.right_heap))


        

    def findMedian(self):
        """
        :rtype: float
        """

        if len(self.right_heap) == len(self.left_heap):
            return (-self.left_heap[0] + self.right_heap[0])/2.0
        else:
            return (-self.left_heap[0])
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()