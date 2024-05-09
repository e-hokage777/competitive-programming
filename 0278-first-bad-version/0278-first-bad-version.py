# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        l = 1
        r = n
        first_bad = 1
        while l <= r:
            mid = l + (r-l)//2
            is_bad = isBadVersion(mid)
            if is_bad:
                first_bad = mid
                r = mid - 1
            else:
                l = mid + 1

        return first_bad
        