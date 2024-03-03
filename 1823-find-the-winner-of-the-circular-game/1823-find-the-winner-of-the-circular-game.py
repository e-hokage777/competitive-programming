class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        persons = [i+1 for i in range(n)]
        index = 0
        while len(persons) > 1:
            index = (index + k-1)%n
            persons.pop(index)
            n = len(persons)

        return persons[0]




        # eliminated = set()
        # i = 0
        # j = k
        # while(len(eliminated) < n-1):
        #     if i not in eliminated:
        #         j -= 1

        #     if j <= 0:
        #         eliminated.add(i)
        #         j = k

        #     i = (i+1)%n


        # for m in range(n):
        #     if m not in eliminated:
        #         return m+1
