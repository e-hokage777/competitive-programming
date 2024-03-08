class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        current_num = nums[0]
        current_num_count = 0
        replace = "_"
        p = -1
        for i in range(len(nums)):

            if nums[i] == current_num:
                if current_num_count >= 2:
                    nums[i] = replace
                    if p == -1 : p = i
                else:
                    current_num_count += 1
            else:
                current_num = nums[i]
                current_num_count = 1


        s = p
        while s < len(nums):
            if nums[s] != replace:
                nums[p], nums[s] = nums[s], nums[p]
                p += 1

            s+=1

        return p
        