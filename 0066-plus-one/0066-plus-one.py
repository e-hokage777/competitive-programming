class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 0
        ## taking care of last digit
        if digits[-1] == 9:
            carry = 1
            digits[-1] = 0
        else:
            digits[-1] += 1


        for i in range(2, len(digits)+1):
            i*=-1
            print(i)
            if carry == 1:
                if digits[i] == 9:
                    digits[i] = 0
                    carry = 1
                else:
                    digits[i] += 1
                    carry = 0
            else:
                break

        if carry == 1:
            digits.insert(0, 1)

        return digits

        