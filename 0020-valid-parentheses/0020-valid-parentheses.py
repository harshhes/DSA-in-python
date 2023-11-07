class Solution:
    def isValid(self, s: str) -> bool:
        pointer = {')': '(', ']': '[', '}': '{'}
        
        stack = []
        
        for i in s:
            if i in pointer:
                
                if stack and stack[-1] == pointer[i]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(i)
                
        return not stack
            