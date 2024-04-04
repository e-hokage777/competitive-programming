class Solution(object):
    def constructProductMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """

        
        prefix_pdt = [1]
        suffix_pdt = [1]
        r,c = len(grid), len(grid[0])
        for i in range(r*c):
            rp = i//c
            cp = i%c
            prefix_pdt.append((grid[rp][cp]*prefix_pdt[-1])%12345)
            suffix_pdt.append((grid[r-rp-1][c-cp-1]*suffix_pdt[-1])%12345)

        prefix_pdt.append(1)
        suffix_pdt.append(1)


        for i in range(r*c):
            rp = i//c
            cp = i%c

            grid[rp][cp] = prefix_pdt[i]*suffix_pdt[-i-3]%12345


        return grid


        