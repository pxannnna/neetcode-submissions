class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # 1, 2, 1, 2, 1, 1, 1
        #len = 7
        # num1 num2
        memo = {} #memoize 

        def dfs(idx):
            if idx >= len(cost):
                return 0
            if idx in memo:
                return memo[idx]

            
            memo[idx] = cost[idx] + min(dfs(idx+1), dfs(idx+2))
            return memo[idx]

        return min(dfs(0), dfs(1))


        