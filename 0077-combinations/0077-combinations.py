class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(j, arr):
            if len(arr) == k:
                result.append(arr[:])
                return

            for i in range(j, n+1):
                arr.append(i)
                backtrack(i+1, arr)
                arr.pop()

        backtrack(1, [])

        return result

        