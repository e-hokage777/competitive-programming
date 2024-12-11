class ListNode:
    def __init__(self,val=None):
        self.next = None
        self.prev = None
        self.val = val

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums = list(set(nums))
        val_to_index = dict()

        for index, value in enumerate(nums):
            nums[index] = ListNode(value)
            val_to_index[value] = index

        
        for node in nums:
            left = node.val - 1
            right = node.val + 1

            if left in val_to_index:
                left_node = nums[val_to_index[left]]
                node.prev = left_node
                left_node.next = node
            if right in val_to_index:
                right_node = nums[val_to_index[right]]
                node.next = right_node
                right_node.prev = node


        max_count = 0

        for node in nums:
            if not node.prev:
                current = node
                count = 0
                while current:
                    count += 1 
                    current = current.next

                max_count = max(max_count, count)

        return max_count
                    

        