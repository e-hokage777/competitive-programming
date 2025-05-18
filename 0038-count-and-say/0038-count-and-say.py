class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        if n == 1:
            return "1"

        runLen = self.countAndSay(n-1)

        holder = []

        current_char = runLen[0]
        count = 0
        for i in range(len(runLen)):
            if runLen[i] != current_char:
                holder.append(str(count) + current_char)
                current_char = runLen[i]
                count = 1
            else:
                count += 1

            if i == len(runLen) - 1:
                holder.append(str(count) + current_char)

        return "".join(holder)
        
        