class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """

        prefix = [0]
        suffix = [0]

        for i in range(k):
            prefix.append(prefix[-1] + cardPoints[i])
            suffix.append(suffix[-1] + cardPoints[-i-1])

        max_sum = 0
        for i in range(k+1):
            max_sum = max(max_sum, prefix[i] + suffix[-i-1])

        return max_sum
        