class Solution(object):
    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        path = []

        def build_path(n,k):

            if n == 0:
                return k

            k = build_path(n-1, k)
            path.append(k)
            return (k+1)//2 if k%2 else k//2

        build_path(n,k)
        current = 0
        for i in range(len(path)-2, -1, -1):
            if current == 0:
                current = 1 if path[i]%2 == 0 else 0
            else:
                current = 0 if path[i]%2 == 0 else 1

        return current

        

        