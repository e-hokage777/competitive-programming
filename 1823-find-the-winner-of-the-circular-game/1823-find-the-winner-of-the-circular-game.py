class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        ar = list(range(1,n+1))

        k_count = 1
        while(len(ar) > 1):
            if k_count != k:
                ar.append(ar[0])
                k_count += 1
            else: k_count = 1

            ar.pop(0)
            # print(ar)


        return ar[0]