class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """

        result = []
        last_j = 0
        for i in range(len(firstList)):
            for j in range(last_j, len(secondList)):
                fl, fr = firstList[i]
                sl, sr = secondList[j]
                intersection = [max(fl, sl), min(fr, sr)]

                if not max(fl, sl) - min(fr, sr) > 0:
                    result.append(intersection)
                    last_j = j

        return result
        