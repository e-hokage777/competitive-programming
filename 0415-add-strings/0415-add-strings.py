class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        carry = 0
        result = []
        for i in range(1, max(len(num1), len(num2)) + 1):
            digit1 = 0
            digit2 = 0
            if i <= len(num1):
                digit1 = int(num1[-i])
            if i <= len(num2):
                digit2 = int(num2[-i])

            _sum = digit1 + digit2 + carry

            

            carry = _sum // 10

            remainder = _sum % 10

            result.append(str(remainder))

        if carry:
            result.append(str(carry))

        return "".join(result[::-1])
        