from collections import deque
class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        """
        :type n: int
        :type leftChild: List[int]
        :type rightChild: List[int]
        :rtype: bool
        """

        #find root
        children = set()
        for i in leftChild:
            children.add(i)
        for i in rightChild:
            children.add(i)

        root = None
        for i in range(n):
            if i not in children:
                root = i
                break

        if root == None:
            return False
        
        visited = [False] * n

        queue = deque([root])
        visited[root]=True

        while queue:
            current = queue.popleft()

            left = leftChild[current]
            right = rightChild[current]


            if left != -1:
                if visited[left]: return False
                queue.append(left)
                visited[left] = True
            if right != -1:
                if visited[right]: return False
                queue.append(right)
                visited[right] = True

        return all(visited)


        