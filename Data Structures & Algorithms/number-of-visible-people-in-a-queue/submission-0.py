class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = [0] * n
        stack = [] # Will store indices
        
        # Iterate backwards from right to left
        for i in range(n - 1, -1, -1):
            count = 0
            # Pop everyone shorter than the current person
            while stack and heights[stack[-1]] < heights[i]:
                stack.pop()
                count += 1
            
            # If there's still someone left in the stack, they are taller 
            # and can be seen by the current person as well.
            if stack:
                count += 1
                
            res[i] = count
            stack.append(i)
            
        return res
