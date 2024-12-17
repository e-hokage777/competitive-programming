class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """

        smallests = []
        largests = []

        for i in range(len(arrays)):
            smallests.append((arrays[i][0],i))
            largests.append((arrays[i][-1],i))

        smallests.sort()
        largests.sort()

        ans = 0

        if smallests[0][-1] != largests[-1][-1]:
            ans = abs(smallests[0][0] - largests[-1][0])
        else:
            ans = abs(smallests[0][0] - largests[-2][0])

        ans = max(abs(smallests[0][0]-largests[-1][0]), ans)

        return ans


        