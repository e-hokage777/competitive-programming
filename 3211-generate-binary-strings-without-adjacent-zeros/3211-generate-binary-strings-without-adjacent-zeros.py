class Solution(object):
    def validStrings(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        self.ans = []

        def backtracking(string):
            if len(string) == n:
                self.ans.append("".join(string))
                return

            if string[-1] == "1":
                string.append("0")
                backtracking(string)
                string.pop()
                string.append("1")
                backtracking(string)
                string.pop()
            else:
                string.append("1")
                backtracking(string)
                string.pop()

        backtracking(["0"])
        backtracking(["1"])

        return self.ans

            
