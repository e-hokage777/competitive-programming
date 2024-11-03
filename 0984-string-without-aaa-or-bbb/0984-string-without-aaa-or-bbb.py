class Solution(object):
    def strWithout3a3b(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: str
        """

        result = []

        while a > 0 or b > 0:
            if a > b:
                if a-b > 1:
                    result.append("aa")
                    a-=2
                else:
                    result.append("a")
                    a-=1

                if b:
                    b-=1
                    result.append("b")
            else:
                if b-a > 1:
                    result.append("bb")
                    b-=2
                else:
                    result.append("b")
                    b-=1

                if a:
                    a-=1
                    result.append("a")

        return "".join(result)


        