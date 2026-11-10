class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {} 
        #O(n*m)

        def dfs(i, a):
            if a == amount:
                return 1

            if a > amount:
                return 0

            if i == len(coins): #out of bounds
                return 0

            if (i, a) in cache:
                return cache[(i,a)]

            cache[(i,a)] = dfs(i, a + coins[i]) + dfs(i+1, a) #choosing a coin at index + skipping the coinf at index i
            return cache[(i,a)]
            
        return dfs(0,0)




        