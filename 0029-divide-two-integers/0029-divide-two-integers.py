class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
 
        polarity = 1

        if (divisor < 0 and dividend > 0) or (divisor > 0 and dividend < 0):
            polarity = -1


        if dividend > 0:
            dividend = -dividend
        if divisor > 0:
            divisor = -divisor

        divisor_temp = divisor
        num_doubles = 0

        while dividend < divisor_temp:
            divisor_temp <<= 1
            num_doubles += 1


        times = 0
        while dividend <= divisor:
            if dividend <= divisor_temp:
                times += 2**num_doubles
                dividend -= divisor_temp
            
            divisor_temp >>= 1
            num_doubles -= 1

        
        # return times * polarity
        if polarity > 0:
            return min(times, 2**31-1)
        else:
            return polarity * times


         
        