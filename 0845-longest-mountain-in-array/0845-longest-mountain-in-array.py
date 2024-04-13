class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        max_len = 0
        for i in range(len(arr)):
            if i > 0 and i < len(arr)-1 and arr[i] > arr[i+1] and arr[i] > arr[i-1] :
                l=r=i
                while r < len(arr) - 1 and arr[r] > arr[r+1]:
                    r+=1 
                while l > 0 and arr[l] > arr[l-1]:
                    l-=1

                max_len = max(max_len,r-l+1) 

        return max_len
        