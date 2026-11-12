class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #monatonic stack
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i in range(n-1, -1, -1):
            t = temperatures[i]
            

            while stack and temperatures[stack[-1]] <= t:
                stack.pop()
            #if stack isnt empty-> top of the stack is the warmer day
            if stack:
                res[i] = stack[-1] - i #days until warmer day
            
            stack.append(i) #push carrent day index 

        return res

            

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        res = [0]* len(temperatures)
        stack = [] # pair: [temp, index]
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t,i])
        return res