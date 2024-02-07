class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """

        word1_new = []
        word2_new = []

        for i in range(len(word1)):
            for j in range(len(word1[i])):
                word1_new.append(word1[i][j])

        for i in range(len(word2)):
            for j in range(len(word2[i])):
                word2_new.append(word2[i][j])

        return word1_new == word2_new