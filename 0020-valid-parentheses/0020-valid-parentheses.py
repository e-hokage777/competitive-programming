class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c in ["(", "{", "["]:
                stack.append(c)
            else:
                if len(stack) < 1:
                    return False
                elif c=="]" and stack[-1] != "[":
                    return False
                elif c=="}" and stack[-1] != "{":
                    return False
                elif c==")" and stack[-1] != "(":
                    return False
                else:
                    stack.pop()

        return len(stack) == 0
        