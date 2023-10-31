class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        mapDict={}
        for i in nums:
            if i in mapDict:
                mapDict[i] += 1
                if mapDict[i] > 1:
                    return True
            mapDict[i] = 1    
        
        return False    