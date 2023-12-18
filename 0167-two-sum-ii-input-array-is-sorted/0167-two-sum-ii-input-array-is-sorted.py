class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = 0
        e = len(numbers) - 1
        curr_sum = 0
        
        while s<e:
            curr_sum = numbers[s] + numbers[e]
            
            if curr_sum < target:
                s += 1
                
            elif curr_sum > target:
                e -= 1
                
            else:
                return [s+1, e+1]