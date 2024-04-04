class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        s = [ord(c) - 97 for c in s]
        prefix = [0]*(len(s)+1)

        for l,r,d in shifts:
            if d == 0:
                prefix[l] -= 1
                prefix[r+1] += 1
            else:
                prefix[l] += 1
                prefix[r+1] -= 1

        for i in range(1, len(prefix)):
            prefix[i]+=prefix[i-1]


        s = [chr(97 + (s[i]+prefix[i]) %26 ) for i in range(len(s))]  

        return "".join(s)    

        