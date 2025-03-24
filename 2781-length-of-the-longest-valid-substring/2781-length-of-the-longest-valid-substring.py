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
        if not string: return -1
        index = 0
        if not self.root[self.index(string[0])]:
            return -1

        current_node = self.root[self.index(string[0])]

        for i in range(1, len(string)):
            character = string[i]

            if not current_node.children[self.index(character)]:
                return -1
            
            current_node = current_node.children[self.index(character)]
            index += 1

        if current_node.is_end:
            return index
        
        return -1
            


class Solution(object):
    def longestValidSubstring(self, word, forbidden):
        """
        :type word: str
        :type forbidden: List[str]
        :rtype: int
        """

        trie = Trie()
        marker = [float("inf")] * len(word)

        for string in forbidden:
            trie.add(string)

        for i in range(len(word)):
            first_letter = word[i]
            for j in range(i, min(i+10, len(word))+1):
                if trie.find(word[i:j]) > -1:
                    marker[i] = min(marker[i], j-i)

        ans = 0
        length = 0
        for i in range(len(marker)):
            if marker[i] == float('inf'):
                length += 1
            else:
                extra = marker[i]-1
                for k in range(i+1,min(len(marker), i + marker[i])):
                    if k + marker[k]-1 <= i + marker[i] - 1:
                        extra = k-i + marker[k]-1
                        break ## once you find the first one break

                length += extra
                ans = max(length, ans)
                length = 0


        return max(ans, length)


            

        ## construct a trie with forbidden strings
        ## loop through [word] and with each letter in [word] as a starting point
        ## check if you can build a letter in forbidden, if you can, then that substring
        ## comes to an end and is in valid
        ## move on to the next character and repeat

        