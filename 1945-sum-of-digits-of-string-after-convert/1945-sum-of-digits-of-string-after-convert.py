class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        transformed_s = "".join(str(ord(letter)-96) for letter in s)
        print(transformed_s)
        for i in range(k):
            transformed_s = self.transform(transformed_s)

        return transformed_s


    def transform(self, number):
        number = str(number)
        return sum([int(x) for x in number])
        