# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def spiralMatrix(self, m, n, head):
        """
        :type m: int
        :type n: int
        :type head: Optional[ListNode]
        :rtype: List[List[int]]
        """

        grid = [[-1] * n for _ in range(m)]
        def fill(current, start_r, end_r, start_c, end_c, step_r, step_c):
            for r in range(start_r, end_r, step_r):
                for c in range(start_c, end_c, step_c):
                    if not current: return None
                    grid[r][c] = current.val
                    current = current.next
            
            return current

        rlim = 0
        clim = 0
        current = head


        while current:
            current = fill(current, rlim, rlim+1, clim, n-clim, 1, 1)
            current = fill(current, rlim+1, m-rlim, n-clim-1,n-clim,1, 1)
            current = fill(current, m-rlim-1, m-rlim, n-clim-2, clim-1, 1, -1)
            current = fill(current, m-rlim-2, rlim, clim, clim+1, -1, 1)


            rlim += 1
            clim += 1
            

        return grid

        