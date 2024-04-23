import math
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for character in tokens:
            if character == "+":
                stack.append(stack.pop() + stack.pop())
            elif character == "*":
                stack.append(stack.pop() * stack.pop())
            elif character == "/":
                b = stack.pop()
                a = stack.pop()

                div = a/b

                if div < 0:
                    stack.append(-1 * (abs(a)//abs(b)))
                else:
                    stack.append(a//b)

            elif character == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a-b)
            else:
                stack.append(int(character))


        return stack.pop()

        