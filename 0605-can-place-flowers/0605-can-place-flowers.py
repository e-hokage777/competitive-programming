class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        for i in range(len(flowerbed)):
            if not flowerbed[i]:
                if i > 0 and flowerbed[i-1]: continue
                if i < len(flowerbed)-1 and flowerbed[i+1]: continue

                n -= 1
            
        
        return n <= 0
        