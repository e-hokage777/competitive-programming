import math

class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)

        k = int(math.ceil((sqrt(8*target+1)-1)/2)) ## finding minimum moves to pass target
        sum_to_k = (k**2 + k)/2

        delta = sum_to_k - target

        if(delta % 2 == 0):
            return k
        elif ((sum_to_k + k + 1)%2 == 0):
            return k + 1 # last number == k
        else:
            return k + 2 # even + even == odd, hence adding one more guarantees you're adding an odd

        

        
        