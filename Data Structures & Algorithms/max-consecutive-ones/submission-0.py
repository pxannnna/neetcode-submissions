class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        res = 0
        count = 0
        for r in range(len(nums)):
            if nums[r] == 1:
                count += 1
                res = max(res, count)
            else:
                l = r
                count = 0

        return res
        