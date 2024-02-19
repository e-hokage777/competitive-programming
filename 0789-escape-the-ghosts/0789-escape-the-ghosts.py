class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """

        ## get the distance between pacman and the food
        pacman_distance = abs(target[0]) + abs(target[1])
        
        ## get the manhattan distance between each ghost and the target
        distances = []

        for x,y in ghosts:
            distances.append(abs(x-target[0]) + abs(y-target[1]))

        for distance in distances:
            if distance <= pacman_distance: return False
        
        return True