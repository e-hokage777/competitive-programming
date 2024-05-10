class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """

        left = 0
        right = max(abs(heaters[0] - houses[0]), abs(heaters[0] - houses[-1])) + 1

        while left <= right:
            middle = left + (right - left)//2
            can_cover = self.can_cover_all(middle, houses, heaters)

            if can_cover:
                right = middle - 1
            else:
                left = middle + 1

        return left
        
    def can_cover_all(self, radius, houses, heaters):
        current_house = 0

        for heater in heaters:
            while abs(houses[current_house] - heater) <= radius:
                current_house += 1

                ## if all houses covered
                if current_house >= len(houses): return True

        ## if all houses not covered or unable to cover last house with last heater
        if current_house < len(houses) - 1 or abs(houses[current_house] - heaters[-1]) > radius:
            return False
        
        return True

    