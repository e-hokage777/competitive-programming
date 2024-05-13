class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """

        # digit_1 = n//100000
        # sub_1 = digit_1 *100000
        # digit_2 = (n-sub_1)//10000
        # sub_2 = sub_1 + digit_2*10000
        # digit_3 = (n-sub_2)//1000
        # sub_3 = sub_2 + digit_3*1000
        # digit_4 = (n-sub_3)//100
        # sub_4 = sub_3 + digit_4*100
        # digit

        dividend = 100000
        sub = 0
        _sum = 0
        _pdt = 1

        first_zero = True

        for i in range(6):
            digit = (n-sub)//dividend
            sub += (digit*dividend)
            dividend/=10

            _sum+=digit

            if digit != 0: first_zero = False

            if not first_zero:
                _pdt *= digit
                first_zero = False

        return _pdt - _sum

        