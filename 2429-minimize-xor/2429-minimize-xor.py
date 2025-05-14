class Solution(object):
    def minimizeXor(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """

        ## determine number of set bits in num2
        ## convert nums1 to binary
        ## prepare x as binary with all zeros with length equal to nums2
        ## find set bits in nums1_bin and place ones there for x
        ## if there are still set bits, start filling x up from behind by looking for zero places
        ## if all zeros filled and set bits still remain, add more significant set bits

        num_set = 0
        num_bits_num2 = 0
        while num2 > 0:
            num_set += 1 & num2
            num2 >>= 1


            num_bits_num2 += 1
        

        ## finding set bits in num1
        set_indices = []
        num_bits_num1 = 0
        index = 0
        while num1 > 0:
            if num1 & 1:
                set_indices.append(index)
            
            index += 1
            num1 >>= 1
            num_bits_num1 += 1


        # print(set_indices, num_bits_num2, num_bits_num1)

        ## fill set places
        x = [0] * max(num_bits_num2, num_bits_num1)


        i = len(set_indices) - 1
        while num_set > 0 and i >= 0:
            x[-set_indices[i]-1] = 1
            num_set -= 1
            i-=1



        i = len(x) - 1
        while num_set > 0:
            if not x[i]:
                x[i] = 1
                num_set -= 1
            i -= 1



        ans = 0
        power = 0
        for i in range(len(x)-1, -1, -1):
            if x[i]:
                ans += 2 ** power
            power += 1

        return ans


        



        