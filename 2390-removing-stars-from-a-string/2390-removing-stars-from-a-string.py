class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """

        holder = []

        for character in s:
            if character == "*":
                holder.pop()
            else:
                holder.append(character)

        return "".join(holder)
        