class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = 0
        
        while l < r:
            # Calculate current area
            current_area = (r - l) * min(heights[l], heights[r])
            max_area = max(max_area, current_area)
            
            # Always move the pointer with the smaller height
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
                
        return max_area