class Solution(object):
    def smallestNumber(self, num):
        """
        :type num: int
        :rtype: int
        """

        negative = num < 0
        num = str(num)
        num = [int(i) for i in num if i!="-"]
        if negative:
            return -1 * int("".join(list(map(str, sorted(num, reverse=True)))))
        else:
            num.sort()
            smallest_num = []
            for i in num:
                if i!=0 and len(smallest_num) > 0 and smallest_num[0] == "0":
                    smallest_num.insert(0,str(i))
                else:
                    smallest_num.append(str(i))


            return int("".join(smallest_num))



        