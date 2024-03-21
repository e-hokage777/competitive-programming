class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        
        l = 0
        r = 0
        baskets = dict()
        max_len = 0
        while r < len(fruits):
            baskets[fruits[r]] = baskets.get(fruits[r], 0) + 1
            if len(baskets) > 2:
                max_len = max(r-l, max_len)

                while len(baskets) > 2:
                    if baskets[fruits[l]] == 1:
                        del baskets[fruits[l]]
                    else:
                        baskets[fruits[l]] -= 1
                    l+=1

            r+=1 

        return max(max_len, r-l)
