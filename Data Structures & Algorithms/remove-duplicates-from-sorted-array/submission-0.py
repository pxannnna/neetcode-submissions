class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        l = 0  # Index of the last written unique element
        
        for r in range(1, len(nums)):
            # Found a new unique element
            if nums[r] != nums[l]:
                l += 1
                nums[l] = nums[r]
                
        # The number of unique elements is index + 1
        return l + 1