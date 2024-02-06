class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        string = []
        i = -1
        offset = 96
        while i >= -len(s):
            if s[i] == "#":
                string.insert(0,chr(int(s[i-2:i])+offset))
                i-=3
            else:
                string.insert(0,chr(int(s[i])+offset))
                i-=1

        
        return "".join(string)
    


