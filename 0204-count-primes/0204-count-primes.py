class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 0: return 0

        is_prime = [True for _ in range(n+1)]

        is_prime[0] = False 
        is_prime[1] = False 
        is_prime[n] = False
        
        for i in range(2,n):

            if is_prime[i]:
                j = i * i

                while j < n:
                    is_prime[j] = False
                    j += i

        return sum(is_prime)
        