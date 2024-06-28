from collections import deque
class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """


        visited = set()
        for deadend in deadends:
            visited.add(deadend)
        queue = deque(["0000"])
        visited.add("0000")
        count = 1
        while queue:
            length = len(queue)
            for i in range(length):
                current = queue.popleft()
                for i in range(4):
                    first_digit = int(current[i])
                    pos1 = "".join([current[:i],str((first_digit+1)%10), current[i+1:]])
                    pos2 = "".join([current[:i],str((first_digit-1)%10), current[i+1:]])

                    if pos1==target or pos2 == target:
                        return count

                    if pos1 not in visited:
                        queue.append(pos1)
                        visited.add(pos1)
                    if pos2 not in visited:
                        queue.append(pos2)
                        visited.add(pos2)
            count+=1



        return -1
                
        