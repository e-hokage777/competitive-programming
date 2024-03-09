class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """

        people.sort()
        boat_count = 0
        l = 0
        r = len(people)-1

        people_sum = people[r]
        while l <= r:
            if people[l] + people[r] <= limit:
                l+=1
            r-=1

            boat_count += 1


        return boat_count



        