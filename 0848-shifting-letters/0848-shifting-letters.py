class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[int]
        :rtype: str
        """

        s = list(s)
        _sum = 0
        for i in range(len(shifts)-1, -1, -1):
            _sum += shifts[i]
            shifts[i] = _sum
            current = (ord(s[i]) - 97 + shifts[i])%26
            s[i] = chr(current+97)

        return "".join(s)
        