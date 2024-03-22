class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        l = 0
        r = 0
        max_len = 0
        can_del = True
        # while r < len(nums):
        #     # if i meet a zero, look for a 1 that is in front of a zero
        #     if nums[r] == 0:
        #         if not can_del:
        #             max_len = max(max_len, r-l-1)
        #             while nums[l] != 1 and l>0 and nums[l-1] != 0 or l==0:
        #                 l+=1
        #             print(l)
        #             can_del = True

        #         if can_del:
        #             can_del = False
                

        #     r+=1

        # if can_del:
        #     return max(r-l+1, max_len)
        # else:
        #     return max(r-l-1, max_len)

        _sum = 0
        while r < len(nums):
            _sum+=nums[r]
            max_len = max(max_len, r-l-1)
            while _sum < r-l:
                print(l,r)
                _sum-=nums[l]
                l+=1

            r+=1

        return max(r-l-1, max_len)

            
