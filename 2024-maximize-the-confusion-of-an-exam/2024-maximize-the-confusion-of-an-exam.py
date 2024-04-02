class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        """
        :type answerKey: str
        :type k: int
        :rtype: int
        """

        answerKey = list(answerKey)
        holder = {"T":0, "F":0}

        l=r=0
        _max = 0

        while r < len(answerKey):
            holder[answerKey[r]] += 1
            while min(holder.values()) > k:
                holder[answerKey[l]] -= 1
                l+=1

            _max = max(_max, sum(holder.values()))

            r+=1

        return _max
        