class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """

        trips.sort(key=lambda trip: trip[1])

        passed = dict()
        current_capacity = capacity

        for i in range(len(trips)):
            current_capacity -= trips[i][0]

            if current_capacity < 0:
                for k in passed.keys():
                    if k <= trips[i][1]:
                        current_capacity = min(capacity, current_capacity + passed[k])
                        del passed[k]

            if current_capacity < 0:
                return False

            passed[trips[i][2]] = trips[i][0]

        return True

        

        
