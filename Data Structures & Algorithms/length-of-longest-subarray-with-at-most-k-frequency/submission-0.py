class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        countmap = {}
        maxlen = 0
        l = 0

        for r in range(len(nums)):
            # 1. Add the current element to the window
            countmap[nums[r]] = countmap.get(nums[r], 0) + 1
            
            # 2. If the frequency exceeds k, shrink from the left until valid
            while countmap[nums[r]] > k:
                countmap[nums[l]] -= 1
                l += 1
                
            # 3. Calculate the max length of the valid window
            maxlen = max(maxlen, r - l + 1)
            
        return maxlen
