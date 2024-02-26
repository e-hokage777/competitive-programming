class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.current = 0
        self.strs = [0] * n
        

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        idKey = idKey - 1
        self.strs[idKey] = value
        result = []

        if idKey == self.current:
            while idKey < len(self.strs) and self.strs[idKey] != 0:
                result.append(self.strs[idKey])
                idKey+=1
            
            self.current = idKey

        return result


        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)