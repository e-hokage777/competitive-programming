# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """
#
#    def length(self):
#        """
#        :rtype int
#        """

class Solution(object):
    def findInMountainArray(self, target, mountain_arr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        
        ## finding peak
        left = 0
        right = mountain_arr.length() -1

        while left < right:
            middle = left + (right-left)//2

            if mountain_arr.get(middle) > mountain_arr.get(middle+1):
                right = middle
            else:
                left = middle + 1

        print("here")
        ## search for taret in first half
        res = self.find_target(0, right, mountain_arr, target)

        if res != -1:
            return res

        ## search right target
        res = self.find_target_reverse(right, mountain_arr.length()-1, mountain_arr, target)

        return res

        

    def find_target(self, left, right, mountain_arr, target):
        
        while left <= right:
            middle = left + (right - left)//2

            value = mountain_arr.get(middle)
            if value == target:
                return middle
            elif target > value:
                left = middle + 1
            else:
                right = middle - 1

        return -1

    def find_target_reverse(self, left, right, mountain_arr, target):
        
        while left <= right:
            middle = left + (right - left)//2

            value = mountain_arr.get(middle)
            if value == target:
                return middle
            elif target < value:
                left = middle + 1
            else:
                right = middle - 1

        return -1
