class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        res = 0
        curSum = 0
        prefixSums = {0:1}

        for n in nums:
            curSum += n
            diff = curSum - k

            res += prefixSums.get(diff,0) #checks if there is an appropriate prefix available that we can cut off, if not return 0, if yes add to total count of ways to get k
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)

        return res

        