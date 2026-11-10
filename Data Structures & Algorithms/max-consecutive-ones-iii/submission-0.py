class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # left and right pointer
        #r ight pointer exanding the window 
        # left shrinking the window
        # when number of 0s inside the window >k -> update result move left pointer -> reduce the number of 0s back to allowed
        #when r reaches the end return res
        res = 0
        l = 0
        count = 0
        numofzero = 0

        for r in range(len(nums)):
            if nums[r] == 1:
                count += 1

            if nums[r] == 0:
                numofzero += 1
                count += 1
                if numofzero > k:
                    res = max(res, count - 1)
                    while nums[l] != 0:
                        l += 1
                        count -= 1
                    l += 1
                    count -= 1
                    numofzero -= 1
        res = max(res, count)
        return res



                



        