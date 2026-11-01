class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sumSoFar = 0
        largestsum = nums[0]
        for n in nums:
            if sumSoFar < 0:
                sumSoFar = 0
            sumSoFar += n
            largestsum = max(sumSoFar, largestsum)
        return largestsum
        