class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """


        def count_but_max(d):
            max_count = float("-inf")
            max_char = None
            _sum = 0

            for k,v in d.items():
                _sum += v

                if v > max_count:
                    max_count = v
                    max_char = k

            return _sum - max_count
        
        holder = dict()

        left = 0
        right = 0
        max_len = -1

        while right < len(s):
            holder[s[right]] = holder.get(s[right], 0) + 1

            while len(holder) > 1:
                if count_but_max(holder) <= k:
                    break
                if holder[s[left]] == 1: del holder[s[left]]
                else: holder[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

            right += 1

        return max_len


