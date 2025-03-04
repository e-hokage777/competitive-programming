from collections import Counter

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """

        counter = Counter(s)
        counts = sorted(counter.items(), key=lambda x: x[1], reverse=True)

        ans = []
        for k,v in counts:
            ans.append(k * v)

        return "".join(ans)


        