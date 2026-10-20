class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()

        def dfs(i, current_sum):
            if current_sum == target:
                res.append(subset.copy())
                return
            if i >= len(candidates):
                return

            
            if current_sum > target:
                return

            subset.append(candidates[i])
            dfs(i+1, current_sum + candidates[i])
            subset.pop()

            next_i = i+1
            while next_i < len(candidates) and candidates[next_i] == candidates[i]:
                next_i += 1

            dfs(next_i, current_sum)
        dfs(0, 0)
        return res