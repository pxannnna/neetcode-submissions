class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} #val: index
        for i,c in enumerate(nums):
            difference = target - c
            if difference in prevMap:
                return [prevMap[difference], i]
            prevMap[c] = i