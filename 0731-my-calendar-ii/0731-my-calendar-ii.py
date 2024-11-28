class MyCalendarTwo(object):

    def __init__(self):
        self.bookings = []
        self.doubles = []

    def book(self, startTime, endTime):
        """
        :type startTime: int
        :type endTime: int
        :rtype: bool
        """

        for s2, e2 in self.doubles:
                if self.intersect(s2,e2, startTime, endTime): return False

        for s1, e1 in self.bookings:
            intersection =  self.intersect(s1, e1, startTime, endTime)
            if intersection:
                self.doubles.append(intersection)
                

        self.bookings.append((startTime, endTime))
        return True

    def intersect(self, s1, e1, s2, e2):
        if s1 <= s2 < e1:
            return (s2, min(e2,e1))
        elif s1 < e2 <= e1:
            return (max(s2,s1), e2)
        elif s2 <= s1 < e2:
            return (s1, min(e2,e1))
        elif s2 < e1 <= e2:
            return (max(s2,s1), e1)

        return False
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)