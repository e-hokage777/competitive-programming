class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """

        if n == 1:
            return 1

        holder = dict()
        does_trust = set()

        for a,b in trust:
            holder[b] = holder.get(b, 0) + 1
            does_trust.add(a)

        for k in holder.keys():
            if holder[k] == n-1 and k not in does_trust:
                return k

        return -1

        