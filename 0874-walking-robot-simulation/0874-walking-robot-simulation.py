class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        robot_x, robot_y = 0,0

        directions = [(0,1), (1,0), (0,-1), (-1, 0)]
        current_index = 0

        obstacles = set((a,b) for a,b in obstacles)
        ans = 0

        for command in commands:
            if command == -2:
                current_index = 3 if current_index - 1 < 0 else current_index - 1
            elif command == -1:
                current_index = (current_index + 1)%4
            else:
                dx, dy = directions[current_index]
                while command and not (robot_x + dx, robot_y + dy) in obstacles:
                    robot_x += dx
                    robot_y += dy
                    command -= 1
            ans = max(robot_x*robot_x + robot_y*robot_y, ans)

        return ans
                