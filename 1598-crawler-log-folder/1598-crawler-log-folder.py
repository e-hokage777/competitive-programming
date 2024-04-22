from collections import deque
class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """

        stack = deque()

        for operation in logs:
            if operation == "../":
                if len(stack) > 0:
                    stack.pop()
            elif operation != "./":
                stack.append(1)
            
        return len(stack)

        