class Solution(object):
    def arrayChange(self, nums, operations):
        """
        :type nums: List[int]
        :type operations: List[List[int]]
        :rtype: List[int]
        """

        operations_dict = dict()
        inv_operations_dict = dict()

        for num, operation in operations:
            if num in inv_operations_dict:
                operations_dict[inv_operations_dict[num]] = operation
                inv_operations_dict[operation] = inv_operations_dict[num]
            else:
                operations_dict[num] = operation
                inv_operations_dict[operation] = num

        for i in range(len(nums)):
            if nums[i] in operations_dict:  
                nums[i] = operations_dict[nums[i]]


        return nums
            
        