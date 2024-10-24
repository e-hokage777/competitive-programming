class TrieNode:
    def __init__(self):
        self.children = dict()
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = TrieNode()
            current = current.children[letter]
    
    def longest_common_prefix(self):
        common_prefix = []

        current = self.root

        while len(current.children) == 1:
            letter, child = current.children.items()[0]
            current = child
            common_prefix.append(letter)

        return "" if not common_prefix else "".join(common_prefix)

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        trie = Trie()

        for word in strs:
            if word == "": return ""
            trie.insert(word)

        return trie.longest_common_prefix()