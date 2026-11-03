import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        ans = right

        while left <= right:
            mid = (left + right) // 2
            
            # Compute total hours required at speed 'mid'
            total_time = sum(math.ceil(pile / mid) for pile in piles)

            if total_time <= h:
                ans = mid        # 'mid' works, check for a smaller speed
                right = mid - 1
            else:
                left = mid + 1   # 'mid' is too slow, increase speed

        return ans
