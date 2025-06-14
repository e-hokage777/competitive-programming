class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

        words = s.split(" ")
        mapping = {}
        words_taken = set()

        if(len(pattern)) != len(words): return False
        
        for i in range(len(pattern)):
            current_pattern = pattern[i]
            current_word = words[i].strip()
            if current_pattern in mapping:
                if mapping[current_pattern] != current_word:
                    return False
            else:
                if current_word in words_taken:
                    return False
                mapping[current_pattern] = current_word
                words_taken.add(current_word)

        return True
        