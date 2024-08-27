class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        result = []

        for i in range(n+1):
            result.append(self.count(i))

        return result

    def count(self, val):
        count = 0
        while val > 0:
            if val%2:
                count += 1
            val = val//2

        return count
        