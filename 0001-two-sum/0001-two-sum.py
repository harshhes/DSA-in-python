class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mapDict = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in mapDict:
                return [mapDict[diff], i]
            mapDict[n] = i