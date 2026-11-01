class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {} # cardinality
        ans = 0
        

        def dfs(idx: int): # N * N^2 => N^3
            nonlocal ans

            if idx in memo:
                return memo[idx]

            res = 1
            for i in range(idx + 1, len(nums)):
                if nums[i] > nums[idx]:
                    #include the number
                    res = max(res, 1 + dfs(i))

            memo[idx] = res
            ans = max(res, ans)

            return res

        for i in range(len(nums)):
            dfs(i)
            
        return ans