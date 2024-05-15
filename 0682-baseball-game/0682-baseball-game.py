class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """

        total_score = 0
        holder = []

        for op in operations:
            if op == "+":
                total_score += (holder[-1] + holder[-2])
                holder.append(holder[-1] + holder[-2])
            elif op == "D":
                total_score += (holder[-1]*2)
                holder.append(holder[-1]*2)
            elif op == "C":
                total_score -= holder.pop()
            else:
                holder.append(int(op))
                total_score += int(op)

        return total_score
        