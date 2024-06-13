class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        holder = []
        def backtrack(index):
            if len(holder) > 2 and holder[-3] + holder[-2] != holder[-1]: return False
            if len(holder) >=3 and index >= len(num): return True

        
            for i in range(index, len(num)):
                holder.append(int(num[index:i+1]))
                if backtrack(i+1):
                    return True
                holder.pop()
                if num[index] == "0": return False

            return False


        return backtrack(0)
        