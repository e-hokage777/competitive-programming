class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        stack = []
        holder = {}

        for n in nums2:
            while len(stack) > 0 and stack[-1] < n:
                holder[stack[-1]] = n
                stack.pop()

            stack.append(n)


        for i in range(len(nums1)):
            if nums1[i] in holder:
                nums1[i] = holder[nums1[i]]
            else:
                nums1[i] = -1

        return nums1

        