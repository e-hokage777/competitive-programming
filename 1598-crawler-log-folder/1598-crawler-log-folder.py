class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """

        # stack = []

        # for operation in logs:
        #     if operation == "../":
        #         if len(stack) > 0:
        #             stack.pop()
        #     elif operation != "./":
        #         stack.append(1)
            
        # return len(stack)

        count = 0
        for operation in logs:
            if operation == "../":
                if count > 0:
                    count-=1
            elif operation != "./":
                count+=1
            
        return count
        