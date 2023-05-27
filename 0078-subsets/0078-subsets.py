class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        final_subsets = [[]]
        
        for i in nums:
            for j in range(len(final_subsets)):
                final_subsets.append(final_subsets[j]+[i])
            
        return final_subsets