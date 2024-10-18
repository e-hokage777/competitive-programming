class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """


        arr = [x%k for x in arr]

        arr = sorted(arr)

        left = 0
        right = len(arr)-1
        zero_count = 0

        while left < right:
            if arr[left] == 0:
                left += 1
                zero_count += 1
                continue

            if arr[left] + arr[right] !=  k: return False
            left += 1
            right -= 1

        if arr[right] == 0: zero_count += 1


        return True if not zero_count%2 else False
        