class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = [] #pair [num, minleft], mono decreasing
        curMin = nums[0]


        if len(nums) < 3:
            return False

        
        #find k that is greater than i
        #find k that is smaller than j

        #havent found? increment k

        for n in nums[1:]:
            while stack and n >= stack[-1][0]:
                stack.pop()
            if stack and n < stack[-1][0] and n > stack[-1][1]:
                return True
            stack.append([n, curMin])
            curMin = min(curMin, n)
        return False




