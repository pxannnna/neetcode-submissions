class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        #create a stack that will store the value and the index
        stack = []
        for n in range(len(nums)):
            if not stack or nums[n] < stack[-1][0]:
                stack.append((nums[n], n))
        distance = 0

        for j in range(len(nums) - 1, -1, -1):
            while stack and stack[-1][0] <= nums[j]:
                val, idx = stack.pop()
                distance = max(distance,j-idx)
        return distance





