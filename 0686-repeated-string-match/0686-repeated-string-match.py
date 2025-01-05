class Solution(object):
    def repeatedStringMatch(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """

        times = len(b)//len(a) + 1
        rep_a = a*(times)
        endpoint = -1
        done = False

        for i in range(len(rep_a) - len(b) + 1):
            a_pointer = i
            b_pointer = 0

            while rep_a[a_pointer] == b[b_pointer]:
                if b_pointer == len(b) - 1:
                    endpoint = a_pointer
                    done = True
                    break

                b_pointer += 1
                a_pointer += 1

            if done:
                break

        if endpoint == -1: return -1
        
        if rep_a[endpoint+1:] == a:
            return times - 1
        return times
        