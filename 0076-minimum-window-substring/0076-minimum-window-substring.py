from collections import Counter, defaultdict
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        t_matcher = Counter(t)
        holder = defaultdict(int)
        true_count = 0
        left, right = 0, 0
        min_len = float("inf")
        min_right = 0
        min_left = 0

        while right < len(s):
            character = s[right]
            if character in t_matcher:
                holder[character] += 1
                true_count += 1 if t_matcher[character] == holder[character] else 0

            while true_count == len(t_matcher):
                character = s[left]
                if character in t_matcher:
                    holder[character] -= 1
                    true_count -= 1 if t_matcher[character] > holder[character] else 0
                
                if right - left < min_len:
                    min_len = right - left
                    min_right = right
                    min_left = left

                left += 1


            right += 1

        return "" if min_len == float("inf") else s[min_left:min_right+1]


        