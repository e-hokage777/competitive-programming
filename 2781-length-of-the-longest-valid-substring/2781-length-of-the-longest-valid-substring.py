class TrieNode:
    def __init__(self, val=None):
        self.val = val
        self.is_end = False
        self.children = [None] * 26

class Trie:
    def __init__(self):
        self.root = [None] * 26

    def index(self, letter):
        return ord(letter) - ord("a")

    def add(self, string):
        if not string: return

        if not self.root[self.index(string[0])]:
            self.root[self.index(string[0])] = TrieNode(string[0])

        current_node = self.root[self.index(string[0])]

        for i in range(1, len(string)):
            character = string[i]
            # if character not in current_node.children:
            if not current_node.children[self.index(character)]:
                current_node.children[self.index(character)] = TrieNode(character)
            
            current_node = current_node.children[self.index(character)]

        current_node.is_end = True

    def find(self, string):
        if not string: return False
        index = 0
        if not self.root[self.index(string[0])]:
            return False

        current_node = self.root[self.index(string[0])]

        for i in range(1, len(string)):
            character = string[i]

            if not current_node.children[self.index(character)]:
                return False
            
            current_node = current_node.children[self.index(character)]
            index += 1

        if current_node.is_end:
            return True
        
        return False
            


class Solution(object):
    def longestValidSubstring(self, word, forbidden):
        """
        :type word: str
        :type forbidden: List[str]
        :rtype: int
        """

        trie = Trie()

        for string in forbidden:
            trie.add(string)

        
        right = len(word) - 1
        ans = 0
        for left in range(len(word)-1, -1, -1):
            valid = True
            for i in range(left, min(left+10, right+1)):
                if trie.find(word[left:i+1]):
                    right = i - 1
                    valid = False
                    break
            
            if valid:    
                ans = max(right - left + 1, ans)


        return ans


            

        ## construct a trie with forbidden strings
        ## loop through [word] and with each letter in [word] as a starting point
        ## check if you can build a letter in forbidden, if you can, then that substring
        ## comes to an end and is in valid
        ## move on to the next character and repeat

        