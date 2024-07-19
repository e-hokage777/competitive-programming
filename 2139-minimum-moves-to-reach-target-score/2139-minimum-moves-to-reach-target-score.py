from collections import deque
class Solution(object):
    def minMoves(self, target, maxDoubles):
        """
        :type target: int
        :type maxDoubles: int
        :rtype: int
        """
        
        moves = 0
        while maxDoubles and target != 1:
            if target%2:
                target -= 1
                moves += 1
            else:
                target/=2
                moves+=1
                maxDoubles-=1

        return moves + (target-1)






        