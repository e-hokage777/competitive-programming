class MyCalendar(object):

    def __init__(self):
        self.bookings = []

    def book(self, startTime, endTime):
        """
        :type startTime: int
        :type endTime: int
        :rtype: bool
        """

        for booked_start, booked_end in self.bookings:
            if startTime >= booked_start and startTime < booked_end:
                return False
            if endTime > booked_start and endTime <= booked_end:
                return False
            if booked_start >= startTime and booked_start < endTime:
                return False
            if booked_end > startTime and booked_end <= endTime:
                return False

        print([startTime, endTime])
        self.bookings.append([startTime, endTime])
        
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)