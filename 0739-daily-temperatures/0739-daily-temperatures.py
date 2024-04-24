class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        holder = dict()
        stack = []
        result = []
        for i in range(len(temperatures)):
            while len(stack) > 0 and temperatures[i] > stack[-1][1]:
                holder[stack[-1][0]] = i - stack[-1][0]
                stack.pop()

            stack.append([i, temperatures[i]])

        for i in range(len(temperatures)):
            if i in holder:
                result.append(holder[i])
            else:
                result.append(0)
        

        return result