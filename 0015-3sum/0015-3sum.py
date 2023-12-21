class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
                
            l,r = i+1, len(nums)-1
            while l<r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                    
                elif threeSum < 0:
                    l += 1
                    
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l<r and nums[l] == nums[l-1]:
                        l += 1
        return ans