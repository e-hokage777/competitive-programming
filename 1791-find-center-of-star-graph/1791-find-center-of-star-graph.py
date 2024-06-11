from collections import defaultdict
class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        holder = defaultdict(int)

        for i,j in edges:
            holder[i]+=1
            holder[j]+=1


        for k in holder.keys():
            if holder[k] == len(edges):
                return k

        