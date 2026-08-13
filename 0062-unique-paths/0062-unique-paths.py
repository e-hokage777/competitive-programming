class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        state_space = [(n) * [float("inf")] for _ in range(m)]

        posx, posy = 0, 0

        state_space[0][0] = 0

        if m > 1:
            state_space[posy+1][0] = 1
        if n > 1:
            state_space[0][posx+1] = 1

        for posy in range(0, m):
            for posx in range(0, n):
                if state_space[posy][posx] != float("inf"):
                    continue

                if posy - 1 >= 0 and posx - 1 >= 0:
                    state_space[posy][posx] = state_space[posy][posx-1] + state_space[posy-1][posx]
                elif posy - 1 < 0:
                    state_space[posy][posx] = state_space[posy][posx-1]
                else:
                    state_space[posy][posx] = state_space[posy-1][posx]


        return max(state_space[m-1][n-1], 1)


        