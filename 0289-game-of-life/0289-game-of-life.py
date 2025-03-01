import copy

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        prevState = copy.deepcopy(board)
        neighbor_positions = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0),
            (1,1),
            (-1,1),
            (1,-1),
            (-1,-1)
        ]

        inbound = lambda r, c: r >= 0 and c >= 0 and r < len(board) and c < len(board[0])

        def processCell(row, column):
            live_count = 0
            n_count = 0
            for dr, dc in neighbor_positions:
                new_r, new_c = row + dr, column + dc
                if inbound(new_r, new_c):
                    live_count += prevState[new_r][new_c]

            if board[row][column]:
                return int(live_count == 2 or live_count == 3)
            
            return int(live_count == 3)

        for r in range(len(board)):
            for c in range(len(board[0])):
                board[r][c] = processCell(r,c)


