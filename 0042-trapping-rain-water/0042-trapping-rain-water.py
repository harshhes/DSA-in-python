class Solution:
    def trap(self, height: List[int]) -> int:
        
        maxLeftarr = []
        maxLeft = 0
        maxRight = 0
        maxRightarr = []
        
        for i in range(len(height)):
            if i==0:
                maxLeftarr.append(maxLeft)
            else:
                maxLeft = max(maxLeft,height[i-1])
                maxLeftarr.append(maxLeft) 
            
        for i in range(len(height)-1, -1, -1):
            if i==len(height)-1:
                maxRightarr.append(maxRight)
            else:
                maxRight = max(maxRight,height[i+1])
                maxRightarr.append(maxRight)
            
        maxRightarr = maxRightarr[::-1]
        res = []
        for i in range(len(height)):
            calc = min(maxLeftarr[i], maxRightarr[i]) - height[i]
            if calc >= 0:
                res.append(calc)
                
        return sum(res)
                
            