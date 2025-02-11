class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """

        ans = [""] * len(indices)

        for i, index in enumerate(indices):
            ans[index] = s[i]

        return "".join(ans)
        