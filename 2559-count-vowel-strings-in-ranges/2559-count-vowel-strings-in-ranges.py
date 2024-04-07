class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """

        vowels = {"a","e","i","o","u"}
        _sum = 0
        for i in range(len(words)):
            value = 0
            if words[i][0] in vowels and words[i][-1] in vowels:
                value = 1

            _sum += value
            words[i] = _sum

        result = []
        
        for s, e in queries:
            if s == 0:
                result.append(words[e])
            else:
                result.append(words[e]-words[s-1])

        return result


        