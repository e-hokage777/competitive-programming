class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        stack = []
        right = 0
        result = 0
        accum = 0
        while right < len(height):
            while stack and stack[-1][2] < height[right]:
                index, max_b, value = stack.pop()

                if stack:
                    stack[-1][1] = max(max_b, value)
                    result += min(height[right], stack[-1][2])*(right - stack[-1][0]-1) - (stack[-1][1])*(right - stack[-1][0]-1)
            

            stack.append([right, 0, height[right]])
            right += 1

        return result

        # while right < len(height):
        #     while stack and stack[-1][2] < height[right]:
        #         index, sum_b, value = stack.pop()
        #         # accum += min(height[right], value)*(right - index - 1) - sum_b

        #         if stack:
        #             stack[-1][1] += (sum_b+value)
        #             accum =  min(height[right], stack[-1][2])*(right - stack[-1][0] - 1) - stack[-1][1]
        #             # accum = max(temp, accum)
        #             # print(stack)

        #     if not stack:
        #         result += accum
        #         accum = 0
            

        #     stack.append([right, 0, height[right]])
        #     right += 1


        # return result + accum


        