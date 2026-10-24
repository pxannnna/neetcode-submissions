class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        
        for i in range(2*len(nums)):
            pointer = i % len(nums)
            ans.append(nums[pointer])
        return ans
