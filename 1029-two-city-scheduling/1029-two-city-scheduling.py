class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """

        citya = []
        cityb = []

        for a,b in costs:
            if a < b:
                citya.append([a,b])
            else:
                cityb.append([a,b])

        print(citya, cityb)

        if len(citya) > len(cityb):
            citya = sorted(citya, key = lambda item: item[1] - item[0], reverse=True)
            while len(citya) > len(cityb):
                cityb.append(citya.pop())
        elif len(cityb) > len(citya):
            cityb = sorted(cityb, key = lambda item: item[0] - item[1], reverse=True)
            while len(cityb) > len(citya):
                citya.append(cityb.pop())

        total_cost = 0

        for i in range(len(citya)):
            total_cost += (citya[i][0] + cityb[i][1])

        return total_cost