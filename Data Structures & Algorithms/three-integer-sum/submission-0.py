class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for a in range(len(nums)):
            if a > 0 and nums[a] == nums[a - 1]:
                continue  # skip duplicate 'a' values

            l, r = a + 1, len(nums) - 1
            while l < r:
                total = nums[a] + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([nums[a], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1  # skip duplicate 'l' values

        return res


        