from collections import defaultdict

class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """

        sums1_2 = []
        sums3_4_holder = defaultdict(int)

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                sums1_2.append(nums1[i] + nums2[j])

        for i in range(len(nums3)):
            for j in range(len(nums4)):
                sums3_4_holder[nums3[i] + nums4[j]] += 1


        ans = 0

        for num in sums1_2:
            ans += sums3_4_holder[-num]

        return ans


        