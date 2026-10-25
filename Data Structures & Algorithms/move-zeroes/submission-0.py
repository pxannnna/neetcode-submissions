class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
        l = 0  # Pointer for the position of the next non-zero element
        
        # 'r' scans through every element in the array
        for r in range(len(nums)):
            if nums[r] != 0:
                # Swap non-zero element to the 'l' position
                nums[l], nums[r] = nums[r], nums[l]
                l += 1




       