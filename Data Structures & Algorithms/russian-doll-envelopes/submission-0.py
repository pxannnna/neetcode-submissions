class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda x: (x[0], -x[1])) 
        #widths ascending, heights descending
        # we sort by width, if width the same, the one with the largest H comes first

        n = len(envelopes)
        def Lis(nums):
            dp = [1] * n
            for i in range(n-1, -1, -1):
                for j in range(i+1, n):
                    if nums[i] < nums[j]:
                        dp[i] = max(dp[i], 1+ dp[j])
            return max(dp)

        return Lis([e[1] for e in envelopes])
