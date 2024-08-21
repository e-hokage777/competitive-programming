class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """

        glasses = [0] * (5050+102)

        glasses[0] = poured*1.0
        n = 0
        for k in range(query_row+1):
            level = k+1
            for index in range(level):
                if glasses[n] > 1:
                    half = (glasses[n] - 1)/2
                    glasses[n+level] += half
                    glasses[n+level+1] += half
                

                if k == query_row and index == query_glass:
                    return min(1, glasses[n])

                n+=1