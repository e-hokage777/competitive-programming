class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        words1 = dict()
        words2 = dict()
        
        for i, word in enumerate(list1):
            words1[word] = words1.get(word, 0) + i
        
        for i, word in enumerate(list2):
            words2[word] = words2.get(word, 0) + i
        
        common = {}
        for word, index in words1.items():
            if word in words2:
                added_index = index + words2[word]
                common[word] = added_index
        sorted(common, key=common.get)
        k = list(sorted(common.items(),key=lambda x:x[1]))
        result = []
        minimum = k[0][1]
        for word, index in k:
            if index == minimum:
                result.append(word)
            else:
                break
        return result
        