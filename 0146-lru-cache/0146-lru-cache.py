from collections import OrderedDict
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        
        self.capacity = capacity
        self.holder = OrderedDict()
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """

        if key in self.holder:
            temp = self.holder[key]
            del self.holder[key]
            self.holder[key] = temp
            return self.holder[key]
        
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """

        if key in self.holder:
            del self.holder[key]
            self.holder[key] = value
        elif len(self.holder) >= self.capacity:
            lru_key = next(iter(self.holder))
            del self.holder[lru_key]

            self.holder[key] = value
        else:
            self.holder[key] = value

        print(self.holder)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)