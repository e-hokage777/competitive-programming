class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        
        ## check if ghosts are closer to goal using manhattain distance
        ## abs(target[0]) + abs(target[1]) = pacman manhattan distance from goal
        for x,y in ghosts:
            if abs(x-target[0]) + abs(y-target[1]) <= abs(target[0]) + abs(target[1]): return False
        
        return True