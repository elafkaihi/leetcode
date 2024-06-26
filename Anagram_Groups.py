class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dictionary = {}
        for word in strs :
            count = [0]*26
            for s in word : 
                count[ord(s)-ord("a")] += 1 
            key = tuple(count)
            if key not in dictionary:
                dictionary[key] = []
            dictionary[key].append(word)
        
        return dictionary.values()