from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        wordList = set(wordList)

        if endWord not in wordList: return 0

        queue = deque([beginWord])

        level = 1

        while queue:
            length = len(queue)
            
            for i in range(length):
                current_word = queue.popleft()

                current_word_list = list(current_word)
                for letter in "abcdefghijklmnopqrstuvwxyz":
                    for i in range(len(current_word_list)):
                        prev_letter = current_word_list[i]

                        if letter != prev_letter:
                            current_word_list[i] = letter
                            new_word = "".join(current_word_list)
                            if new_word == endWord: return level + 1

                            if new_word in wordList:
                                queue.append(new_word)
                                wordList.remove(new_word)

                            current_word_list[i] = prev_letter

            level += 1

        return 0
        