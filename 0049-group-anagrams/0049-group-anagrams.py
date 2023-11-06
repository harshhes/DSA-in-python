class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        words_dict = {}
        
        for word in strs:
            key = tuple(sorted(word))
            words_dict[key] = words_dict.get(key, []) + [word]
            
            
        return words_dict.values()