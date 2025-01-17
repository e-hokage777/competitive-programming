class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """

        self.bit = self.prepare_bit(nums)
        self.nums = nums
        

    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """

        current_val = self.nums[index]
        self.nums[index] = val
        index += 1
        while index <= len(self.bit)-1:
            self.bit[index] += (val-current_val)
            index += (index & -index)
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        # find left
        left_prefix_sum = self.find_prefix_sum(left)
        right_prefix_sum = self.find_prefix_sum(right+1)

        return right_prefix_sum - left_prefix_sum


    def prepare_bit(self, nums):
        bit = [0] * (len(nums)+1)

        for i in range(1, len(bit)):
            index = i
            diff = (index & -index)
            start = index - diff + 1


            bit[index] = sum(nums[start-1:index])

        return bit

    def find_prefix_sum(self, index):
        if index < 0: return 0
        prefix_sum = 0
        while index > 0:
            prefix_sum += self.bit[index]
            index = index - (index & -index)

        return prefix_sum
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)