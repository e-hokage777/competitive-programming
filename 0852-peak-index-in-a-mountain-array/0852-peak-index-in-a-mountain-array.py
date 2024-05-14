class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        left = 0
        right = len(arr)

        while left < right:
            middle = left + (right - left)//2

            if arr[middle] > arr[middle+1]:
                right = middle
            else:
                left = middle + 1

            
        return right
        