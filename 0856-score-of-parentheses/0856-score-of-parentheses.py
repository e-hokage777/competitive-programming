class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        stack = []

        for c in s:
            if c == "(":
                stack.append(0)
            else:
                if len(stack) > 1:
                    t = stack.pop()
                    stack[-1] += max(t*2, 1)
                else:
                    stack.append(max(stack.pop()*2, 1))

        return stack[-1]

        