from collections import defaultdict

class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        # ref_point = (0, 0)
        # distances = [(point[0]-ref_point[0])**2 + (point[1] - ref_point[1])**2 for point in points]
        # print(distances)
        # distances.sort()

        # num_boomerangs = 0


        # for i in range(len(distances)):
        #     for j in range(i+1, len(distances)-1):
        #         diff = distances[j] - distances[i]
        #         third_point =  distances[j] + diff
        #         index = bisect_left(distances, third_point, lo=j+1, hi=len(distances)-1)

        #         if distances[index] == third_point:
        #             num_boomerangs += 2
        
        # return num_boomerangs

        num_boomerangs = 0

        for i in range(len(points)):
            holder = defaultdict(int)
            for j in range(len(points)):
                if i == j:
                    continue
                else:
                    distance = (points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2
                    k = holder[distance]
                    if k >= 1:
                        num_boomerangs += (k + k**2)
                    holder[distance] += 1

        return num_boomerangs




        