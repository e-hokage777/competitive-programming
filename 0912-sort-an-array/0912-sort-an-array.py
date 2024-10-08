class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        def merge(left_half, right_half):
            merged = []
            left_pointer = 0
            right_pointer = 0

            while left_pointer < len(left_half) and right_pointer < len(right_half):
                if left_half[left_pointer] <= right_half[right_pointer]:
                    merged.append(left_half[left_pointer])
                    left_pointer += 1
                else:
                    merged.append(right_half[right_pointer])
                    right_pointer += 1

            merged.extend(left_half[left_pointer:])
            merged.extend(right_half[right_pointer:])

            return merged


        def merge_sort(left, right, arr):
            if left == right: return [arr[left]]

            middle = left + (right-left)//2
            left_half = merge_sort(left, middle, arr)
            right_half = merge_sort(middle+1, right, arr)


            return merge(left_half, right_half)

        return merge_sort(0, len(nums)-1, nums)

        