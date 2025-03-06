class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        return self.form_string(s) == self.form_string(t)

    def form_string(self, string):
        stack = []

        for letter in string:
            if letter == "#":
                if stack:
                    stack.pop()
            else:
                stack.append(letter)
        return "".join(stack)
        