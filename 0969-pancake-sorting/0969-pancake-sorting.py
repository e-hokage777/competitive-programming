class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        flip_indices = []
        current = len(arr)
        for i in range(len(arr)):
            for j in range(len(arr)-i):
                if arr[j] == current:
                    l = 0
                    r = j

                    ## put highest at front
                    flip_indices.append(r + 1)
                    while l < r:
                        arr[l], arr[r] = arr[r], arr[l]
                        l += 1
                        r -= 1


                    ## reverse entire list
                    l = 0
                    r = len(arr) - i - 1


                    flip_indices.append(r + 1)
                    while l < r:
                        arr[l], arr[r] = arr[r], arr[l]
                        l += 1
                        r -= 1 

            current -= 1

        print(arr)
        return flip_indices
            