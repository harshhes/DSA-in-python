class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l,r = 0, len(height) - 1
        
        while l<r:
            area = (r-l) * min(height[r], height[l])
            res = max(area, res)
            
            if height[l] < height[r]:
                l += 1
                
            else:
                r -= 1
                
        return res