class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        POSITIVE_BOUND = str(2**31 - 1)
        NEGATIVE_BOUND = str(2**31)



        x_reversed = str(x)[::-1]

        if(x < 0):
            x_reversed = x_reversed[:-1]
            if len(x_reversed) == len(NEGATIVE_BOUND):
                for i in range(len(NEGATIVE_BOUND)):
                    if int(x_reversed[i]) > int(NEGATIVE_BOUND[i]):
                        return 0
                    if int(x_reversed[i]) < int(NEGATIVE_BOUND[i]):
                        return -1 * int(x_reversed)
            
            return -1 * int(x_reversed)
        else:
            if len(x_reversed) == len(POSITIVE_BOUND):
                for i in range(len(POSITIVE_BOUND)):
                    if int(x_reversed[i]) > int(POSITIVE_BOUND[i]):
                        return 0
                    if int(x_reversed[i]) < int(NEGATIVE_BOUND[i]):
                        return int(x_reversed)

            return int(x_reversed)
            
        
        