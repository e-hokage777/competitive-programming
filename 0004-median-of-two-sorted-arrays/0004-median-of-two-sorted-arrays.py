import bisect

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """


        n = len(nums1) + len(nums2)
        combined_middle = n//2

        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        left = 0
        right = len(nums1) - 1

        while True:
            middle = left + (right-left)//2
            rest = combined_middle - middle - 2


            a1 = nums1[middle] if middle >= 0 else float('-inf')
            a2 = nums1[middle + 1] if middle + 1 < len(nums1) else float('inf')
            b1 = nums2[rest] if rest >= 0 else float('-inf')
            b2 = nums2[rest+1] if rest + 1 < len(nums2) else float("inf")


            if b2 >= a1 and a2 >= b1:
                if n%2:
                    return min(a2, b2)
                return (max(a1, b1) + min(a2, b2))/2.0
            elif a1 > b2:
                right = middle - 1
            else:
                left = middle + 1
                