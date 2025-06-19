class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        visited = set()
        ans = set()

        def recurse(arr):
            if len(visited) == len(nums):
                ans.add(tuple(arr))
                return


            for i in range(len(nums)):
                if i not in visited:
                    visited.add(i)
                    recurse(arr + [nums[i]])
                    visited.remove(i)

        recurse([])
        return list(ans)


            

        