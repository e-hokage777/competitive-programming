class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        target = len(nums) // 3
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        result = []
        for num, frequency in freq.items():
            if frequency > target:
                result.append(num)
                # this is because there can be at most 2 elements
                # that fulfull the criteria
                if len(result) >= 2:
                    break
        return result