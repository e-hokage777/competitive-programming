class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        k = 0
        holder = []
        while k < numRows:
            if k == 0:
                holder.append([1])
                k+=1
                continue

            row = [holder[-1][0]]

            last_row = holder[-1]
            for i in range(len(last_row)-1):
                row.append(last_row[i] + last_row[i+1])
            
            row.append(last_row[-1])

            holder.append(row)

            k += 1

        return holder