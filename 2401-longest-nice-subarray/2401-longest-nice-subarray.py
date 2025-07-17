class Solution(object):
    def longestNiceSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ans = 1
        for i in range(len(nums)):
            holder = 0
            count = 0
            for j in range(i, min(i+30, len(nums))):
                holder = self.test(holder, nums[j])
                if holder  == -1:
                    break
        
                count += 1
            
            ans = max(ans, count)

        return ans
                    

    def test(self, a, b):
        count_extra = True
        extra = 0
        ans = 0
        while a > 0 or b > 0:
            ans <<= 1
            if (a & b) & 1:
                return -1
            elif (a & 1) or (b & 1):
                ans |= 1
                count_extra = False
            else:
                if count_extra:
                    extra += 1

            a >>= 1
            b >>= 1



        actual_ans = 0

        while ans > 0:
            actual_ans <<= 1
            actual_ans |= (ans & 1)
            ans >>= 1

        while extra > 0:
            actual_ans <<= 1
            extra -= 1

        return actual_ans
            

            

                
                    
