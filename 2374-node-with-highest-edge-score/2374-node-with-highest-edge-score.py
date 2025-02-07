from collections import defaultdict
class Solution(object):
    def edgeScore(self, edges):
        """
        :type edges: List[int]
        :rtype: int
        """

        ans = float("inf")
        max_score = float("-inf")
        scores = defaultdict(int)
        
        for i, node in enumerate(edges):
            scores[node] += i

            if scores[node] > max_score:
                ans = node
                max_score = scores[node]
            
            if scores[node] == max_score and node < ans:
                ans = k


        return ans
        