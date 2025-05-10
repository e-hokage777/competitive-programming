from collections import Counter

class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """

        frequencies = Counter(word)
    
        items = [(v, k) for k,v  in  frequencies.items()]
        
        items.sort(reverse=True)


        times = 0
        count = 0

        pushes = 0


        for v,k in items:
            pushes += (1 + times) * v

            count += 1
            times = count // 8


        return pushes






        