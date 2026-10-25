class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        # Initialize your 4 pointers
        left, right = 0, len(height) - 1
        pl, pr = left + 1, right - 1
        trapped = 0
        
        while pl <= pr:
            # Decide which side has the smaller boundary wall
            if height[left] <= height[right]:
                if height[pl] < height[left]:
                    trapped += height[left] - height[pl]
                else:
                    left = pl  # Update left reference wall
                pl += 1
            else:
                if height[pr] < height[right]:
                    trapped += height[right] - height[pr]
                else:
                    right = pr  # Update right reference wall
                pr -= 1
                
        return trapped
