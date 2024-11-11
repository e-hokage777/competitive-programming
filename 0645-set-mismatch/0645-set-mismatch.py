class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        visited = [False]*len(nums)
        result = []

        for num in nums:
            if visited[num-1]:
                result.append(num)
            visited[num-1] = True

        for i in range(len(visited)):
            if not visited[i]:
                result.append(i+1)

        return result
        