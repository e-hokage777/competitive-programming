class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack = []

        for c in s:
            if c in "0123456789" and stack:
                stack.pop()
            else:
                stack.append(c)

        return "".join(stack)
        