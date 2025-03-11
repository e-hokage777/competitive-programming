class Solution(object):
    def maxSumRangeQuery(self, nums, requests):
        """
        :type nums: List[int]
        :type requests: List[List[int]]
        :rtype: int
        """

        marker = [0] * (len(nums) + 1)

        for start, end in requests:
            marker[start] += 1
            marker[end + 1] -= 1

        for i in range(1, len(marker)):
            marker[i] += marker[i-1]


        nums.sort(reverse=True)
        marker.sort(reverse=True)

        ans= 0

        for i in range(len(nums)):
            ans += nums[i] * marker[i]


        return ans % (10**9 + 7)


        