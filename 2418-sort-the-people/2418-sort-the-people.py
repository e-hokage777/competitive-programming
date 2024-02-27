class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """

        ## for first loop 0 to l-1
        swap = False
        for i in range(len(heights)-1):
            for j in range(len(heights)-i-1):
                if heights[j] < heights[j+1]:
                    ## swap
                    heights[j], heights[j+1] = heights[j+1], heights[j]
                    names[j], names[j+1] = names[j+1], names[j]
                    swap = True
            
            if not swap:
                break

        print(heights)
        return names