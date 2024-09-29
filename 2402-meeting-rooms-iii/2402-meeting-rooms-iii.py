from heapq import heappush, heappop
from collections import defaultdict
class Solution(object):
    def mostBooked(self, n, meetings):
        """
        :type n: int
        :type meetings: List[List[int]]
        :rtype: int
        """

        meetings.sort()
        counter = defaultdict(int)
        room_heap = list(range(n))
        ongoing_meeting_heap = []


        time = 0
        
        for i in range(len(meetings)):
            start, end = meetings[i]
            time = max(time, start)

            while ongoing_meeting_heap and time >= ongoing_meeting_heap[0][0]:
                _, room = heappop(ongoing_meeting_heap)
                heappush(room_heap, room)

            if room_heap:
                room = heappop(room_heap)
                heappush(ongoing_meeting_heap, (time+(end-start), room))
                counter[room] += 1
            else:
                meeting_end_time, room = heappop(ongoing_meeting_heap)
                time = meeting_end_time
                heappush(ongoing_meeting_heap, (time + (end-start), room))
                counter[room] += 1



        max_room,max_count = 0,0
        for k,v in sorted(counter.items()):
            if v > max_count:
                max_count = v
                max_room = k
            
        return max_room


        