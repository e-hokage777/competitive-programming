class Solution(object):
    def minimumJumps(self, forbidden, a, b, x):
        """
        :type forbidden: List[int]
        :type a: int
        :type b: int
        :type x: int
        :rtype: int
        """
        ## dp
        ## tree (bfs): each node can be entered in a forward state or a back state (visited)
        forbidden = set(forbidden)
        visited = {(0,False)}
        queue = deque([(0, False)])

        jumps = 0

        while queue:
            length = len(queue)

            for i in range(length):
                current = queue.popleft()
                position, from_back = current

                if position == x: return jumps

                if position > 10e4: continue

                if not (position + a > x and position+a-b > x and a >= b):
                    state = (position+a, False)
                    if state not in visited and (position+a) not in forbidden:
                        queue.append(state)
                        visited.add(state)
                if not from_back and position-b >= 0:
                    state = (position-b, True)
                    if state not in visited and (position-b) not in forbidden:
                        queue.append(state)
                        visited.add(state)

        
            jumps += 1

        return -1