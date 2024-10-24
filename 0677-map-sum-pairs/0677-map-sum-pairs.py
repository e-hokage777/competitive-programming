class TrieNode:
    def __init__(self):
        self.children = dict()
        self.sum = 0

class MapSum(object):

    def __init__(self):
        self.root = TrieNode()
        self.holder = dict()

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """

        if key in self.holder:
            self.overwrite(key, val)
        else:
            current = self.root
            for letter in key:
                if letter not in current.children:
                    current.children[letter] = TrieNode()
                
                current.children[letter].sum += val
                current = current.children[letter]

        self.holder[key] = val


    def overwrite(self, key, new_val):
        old_val = self.holder[key]
        
        if new_val != old_val:
            current = self.root
            for letter in key:
                current.children[letter].sum += (new_val - old_val)
                current = current.children[letter]
        

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """

        current = self.root
        for letter in prefix:
            if letter in current.children:
                current = current.children[letter]
            else: return 0
            # current = current.children[letter]

        return current.sum
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)