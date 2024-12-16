class Solution(object):
    def missingRolls(self, rolls, mean, n):
        """
        :type rolls: List[int]
        :type mean: int
        :type n: int
        :rtype: List[int]
        """

        sum_m = sum(rolls)
        total_rolls = len(rolls) + n
        sum_n = total_rolls*mean - sum_m ## sum of the values from the missing n rolls

        ## impossible if this condition passes
        if sum_n <=0:
            return []

        quotient, remainder = divmod(sum_n, n)

        ## impossible to form if this condition passes)
        if quotient < 1:
            return []
        if quotient > 6:
            return []
        if quotient == 6 and remainder:
            return []

        rolls_n = [quotient] * n

        pos = 0

        ## distribute remainder to rolls
        while remainder > 0:
            sub = min(remainder, 6-rolls_n[pos])
            rolls_n[pos] += sub

            remainder -= sub
            pos += 1

        return rolls_n
        