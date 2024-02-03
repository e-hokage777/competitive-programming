class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        
        c = []
        lw1 = len(word1)
        lw2 = len(word2)
        for i in range(max(lw1, lw2)):
            if i < lw1: c.append(word1[i])
            if i < lw2: c.append(word2[i])

        return "".join(c)