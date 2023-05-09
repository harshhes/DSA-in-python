class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique_results = Counter(nums)
        for key, value in unique_results.items():
            if value == 1:
                return key