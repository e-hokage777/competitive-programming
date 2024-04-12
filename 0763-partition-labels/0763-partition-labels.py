class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """

        found = set()
        forms = True
        l=0
        result = []
        for i in range(len(s)):
            found.add(s[i])
            forms=True
            for j in range(i+1,len(s)):
                if s[j] in found:
                    forms=False
                    break
                
            if forms:
                result.append(i-l+1)
                l=i+1
                found.clear()

        return result

        # while r < len(s):
        #     found.add(s[r])

        