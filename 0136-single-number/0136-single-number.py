class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda total, el: total ^ el, nums)
        # unique_results = Counter(nums)
        # for key, value in unique_results.items():
        #     if value == 1:
        #         return key