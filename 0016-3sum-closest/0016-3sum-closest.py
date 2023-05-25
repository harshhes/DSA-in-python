class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')
        
        for i in range(len(nums) - 2):
            left = i+1
            right = len(nums)-1
            
            while left < right:
                # if left >=len(nums) or right < 0:
                #     break
                curr_sum = nums[i] + nums[left] + nums[right]

                if abs(curr_sum - target) < abs(closest_sum - target):
                    closest_sum = curr_sum
                    
                if curr_sum < target:
                    left += 1
                    
                elif curr_sum > target:
                    right -= 1
                    
                else:
                    return target
                
        return closest_sum