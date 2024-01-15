class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = [] # pairs [[temp, index]]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                temp, index = stack.pop()
                output[index] = i-index


            stack.append([t,i])

        return output