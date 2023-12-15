class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # O(n) time Sol
        ans = 0
        l = 0
        r = len(height) - 1
        
        while l < r:
            area = (r-l) * min(height[l], height[r])
            ans  = max(ans, area)
            
            if height[l] < height[r] or height[l] == height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            # print(area)
            
        return ans
            
        
                