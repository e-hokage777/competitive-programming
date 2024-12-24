from collections import defaultdict, deque
class Solution(object):
    def findTheLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        vowel_mask = {
            "a": 1,
            "e": 2,
            "i": 4,
            "o": 8,
            "u": 16,
        }
        bin_counts = 0
        bin_track = []
        index_holder = dict()
        max_len = 0

        for index, letter in enumerate(s):
            if letter in vowel_mask:
                bin_counts ^= vowel_mask[letter]
            
            if bin_counts == 0:
                max_len = max(max_len, index + 1)
            elif bin_counts not in index_holder:
                index_holder[bin_counts] = index
            else:
                max_len = max(max_len, index - index_holder[bin_counts])

            bin_track.append(bin_counts)

        return max_len



        

        