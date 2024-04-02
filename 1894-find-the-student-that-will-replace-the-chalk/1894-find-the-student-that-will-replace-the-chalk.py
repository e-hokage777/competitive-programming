class Solution(object):
    def chalkReplacer(self, chalk, k):
        """
        :type chalk: List[int]
        :type k: int
        :rtype: int
        """

        remainder = k%sum(chalk)

        _sum = 0
        for i in range(len(chalk)):
            _sum+=chalk[i]

            if _sum > remainder:
                return i
        