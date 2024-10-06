class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        

        stop = 0
        current_diff = None
        result = 0
        for i in range(len(nums)-1):
            if current_diff == None:
                current_diff = nums[i+1] - nums[i]
                stop = i

            else:
                diff = nums[i+1] - nums[i]
                if diff != current_diff:
                    if i - stop >= 2:
                        
                        for k in range(stop, i-1):
                            result += i-k-1

                    current_diff = None


        
        if current_diff != None:
            if len(nums)-1 - stop >= 2:
                for k in range(stop, len(nums)-2):
                    result += len(nums)-k-2

        return result
        