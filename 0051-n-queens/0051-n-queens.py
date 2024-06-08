class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        self.boolean_grid = [[0]*4 for i in range(n)]
        self.result = []
        self.places = []

        def mark_boolean_grid(row, col, val):
            ## marking rows
            for i in range(n):
                self.boolean_grid[row][i] += val
                self.boolean_grid[i][col] += val
            
            for i in range(min(n-col, n-row)):
                self.boolean_grid[row+i][col+i] += val

            for i in range(min(col+1, n-row)):
                self.boolean_grid[row+i][col-i] += val

        def backtrack(row):
            if row >= n:
                ## add to result
                self.result.append(self.places[:])
                return

            for i in range(n):
                if self.boolean_grid[row][i] != 0:
                    continue

                ## place queen there and mark off places 
                self.places.append(i)
                mark_boolean_grid(row, i, 1)
                

                ## call for next row
                backtrack(row+1)

                self.places.pop()
                mark_boolean_grid(row,i,-1)


        backtrack(0)


        answer = []
        for res in self.result:
            temp = []
            k = len(res)
            for inner in res:
                temp2 = ["."]*k
                temp2[inner] = "Q"
                temp.append("".join(temp2))

            answer.append(temp)

        return answer




        