class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestSeq = 0
        
        for n in numSet:
            if (n-1) not in numSet:
                seqLength = 0
                while n+seqLength in numSet:
                    seqLength += 1
                    
                longestSeq = max(seqLength, longestSeq)
                
        return longestSeq