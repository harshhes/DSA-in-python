class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestseq = 0

        for i in nums:
            if i-1 not in numSet:
                seq = 0
                while i+seq in numSet:
                    seq += 1


                longestseq = max(longestseq, seq)

        return longestseq
