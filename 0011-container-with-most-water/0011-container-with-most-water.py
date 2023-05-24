class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        answer = 0
        
        while left <= right:
            area = min(height[right], height[left]) * (right-left)
            answer = max(area,answer)
            
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return answer