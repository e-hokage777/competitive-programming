from collections import defaultdict
class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """

        holder = defaultdict(int)
        pair_holder = set()
        for a,b in roads:
            holder[a] += 1
            holder[b] += 1
            pair_holder.add((a,b))

        max_rank = float("-inf")
        cities = holder.keys()
        for i in range(len(cities)):
            for j in range(i+1,len(cities)):
                rank = holder[cities[i]] + holder[cities[j]]
                if((cities[i],cities[j]) in pair_holder or (cities[j], cities[i]) in pair_holder):
                    rank -= 1

                max_rank = max(max_rank, rank)

        return max_rank

        