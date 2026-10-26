from collections import defaultdict
from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict(int)
        l = 0
        res = 0
        
        for r in range(len(fruits)):
            # 1. Add current fruit at right pointer to basket
            count[fruits[r]] += 1
            
            # 2. If we have more than 2 unique fruit types, shrink window from left
            while len(count) > 2:
                count[fruits[l]] -= 1
                if count[fruits[l]] == 0:
                    del count[fruits[l]]
                l += 1
                
            # 3. Update maximum fruits collected
            res = max(res, r - l + 1)
            
        return res
