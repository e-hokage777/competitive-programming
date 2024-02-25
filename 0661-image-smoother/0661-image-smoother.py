class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        smooth_img = [[0]*len(img[0]) for i in range(len(img))]
        for i in range(len(img)):
            for j in range(len(img[0])):
                _sum = 0
                _count = 0

                for m in range(max(i-1, 0), min(i+1, len(img)-1)+1):
                    for n in range(max(j-1, 0), min(j+1, len(img[0])-1)+1):
                        _sum += img[m][n]
                        _count += 1

                smooth_img[i][j] = _sum//_count

        return smooth_img

                # _sum += img[i][j]

                # if i-1 >= 0:
                #     _sum += img[i-1][j]
                #     _count += 1
                # if i+1 < len(img):
                #     _sum += img[i+1][j]
                #     _count += 1
                # if j-1 >=0:
                #     _sum += img[i][j+1]
                #     _count += 1
                # if j+1 < len(img[0]):
                #     _sum += img[i][j+1]
                #     _count += 1
                # if i-1 >= 0 and j-1 >= 0:
                #     _sum += img[i-1][j-1]
                #     _count+=1
                # if i+1 < len(img) and j+1 < len(img[]):
                #     _sum += img[i-1][j-1]
                #     _count+=1
                

        