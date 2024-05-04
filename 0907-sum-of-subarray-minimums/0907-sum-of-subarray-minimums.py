class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        stack = []
        stack_sum = 0
        min_sum = 0

        for n in arr:
            popped_count = 1
            while stack and n < stack[-1][0]:
                v,c = stack.pop()
                popped_count += c
                stack_sum -= (v*c)

            stack.append([n, popped_count])
            stack_sum += n*popped_count


            min_sum += stack_sum

        return min_sum

        