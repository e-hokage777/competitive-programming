class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        found = {1}
        uglies = [1]
        times = [0]
        while n > 1:
            min_val = float("inf")
            min_index = -1
            for i in range(len(uglies)-1, -1, -1):
                if times[i] == 3: break
                val1 = uglies[i] * 2
                val2 = uglies[i] * 3
                val3 = uglies[i] * 5


                if val1 < min_val and val1 not in found:
                    min_index = i
                    min_val = val1
                if val2 < min_val and val2 not in found:
                    min_index = i
                    min_val = val2
                if val3 < min_val and val3 not in found:
                    min_index = i
                    min_val = val3

            uglies.append(min_val)
            times[min_index] += 1
            found.add(min_val)
            times.append(0)

            n-=1
        return uglies[-1]



        