class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        ans = []
        # holder = []
        def backtracking(holder, num_open, num_close):
            if len(holder) == n * 2:
                if self.test(holder):
                    ans.append("".join(holder))
            
            if num_open:
                holder.append("(")
                backtracking(holder, num_open-1, num_close)
                holder.pop()
                num_open
            if num_close:
                holder.append(")")
                backtracking(holder, num_open, num_close-1)
                holder.pop()

        backtracking([], n, n)

        return ans


    def test(self, holder):
        stack = []
        
        for char in holder:
            if char == "(":
                stack.append("(")
            else:
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    return False

        return not stack



        