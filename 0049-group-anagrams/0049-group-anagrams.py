class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words_list= {}
        
        for word in strs:
            key = tuple(sorted(word))
            words_list[key] = words_list.get(key,[])+[word]
        
        return words_list.values()