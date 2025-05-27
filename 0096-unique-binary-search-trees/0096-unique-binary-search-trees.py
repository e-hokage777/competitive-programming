class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        self.memo = [-1] * (n+1)


        def recurse(n):
            if n == 0:
                return 1
            if n == 1:
                return 1


            count = 0
            for i in range(1,n+1):
                if self.memo[i-1] == -1:
                    self.memo[i-1] = recurse(i-1)
                if self.memo[n-i] == -1:
                    self.memo[n-i] = recurse(n-i)
                

                count += (self.memo[i-1] * self.memo[n-i])

            self.memo[n] = count
            return self.memo[n]

        return recurse(n)



