from collections import defaultdict
class TopVotedCandidate(object):

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        self.persons = persons
        self.times = times

        self.winner_at_time = dict()

        counter = defaultdict(int)
        max_count = 0
        winning_person = 0


        for i in range(len(self.persons)):
            counter[self.persons[i]] += 1
            if counter[self.persons[i]] >= max_count:
                max_count = counter[self.persons[i]]
                winning_person = self.persons[i]
            self.winner_at_time[i] = winning_person
        

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """

        left = -1
        right = len(self.times)

        while right - left > 1:
            middle = left + (right - left)//2

            if t < self.times[middle]:
                right = middle
            else:
                left = middle

        print(right-1,len(self.persons))
        return self.winner_at_time[right-1]

        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)