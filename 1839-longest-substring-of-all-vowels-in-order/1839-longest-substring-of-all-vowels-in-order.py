from collections import defaultdict
class Solution(object):
    def longestBeautifulSubstring(self, word):
        """
        :type word: str
        :rtype: int
        """

        holder = defaultdict(int)
        l=r=max_len=0

        for r in range(len(word)):
            if r != 0 and word[r] < word[r-1]:
                holder = defaultdict(int)
                l=r

            holder[word[r]]+=1
            if len(holder) == 5:
                max_len = max(max_len, r-l+1)

        return max_len



                
