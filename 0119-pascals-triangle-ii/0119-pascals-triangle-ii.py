class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = []
        numerator = self.factorial(rowIndex)

        for i in range(rowIndex+1):
            den1 = factorial(rowIndex-i)
            den2 = factorial(i)
            result.append(numerator/(den1*den2))

        return result


    def factorial(self, n):
        if n == 0: return 1
        return n * factorial(n-1)
