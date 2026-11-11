class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {} # subarray piles (l,r) -> Max Alice Total

        # return: Max alice total

        def dfs(l,r):
            #base case
            #no more leements to choose from
            if l > r:
                return 0
            if (l,r) in dp:
                return dp[(l,r)]

            #if we have even number remaining then its Alice's turn
            #if we have odd number remaining then its Bob's turn

            even = (r-l) % 2 == 0
            left = piles[l] if even else 0 # Alice can chose l or cannot(0)
            right = piles[r] if even else 0#Alice can chose r or cannot (0)


            dp[(l,r)] = max(dfs(l+1, r) + left, dfs(l, r-1) + right)

            return dp[(l,r)]

        total = sum(piles)
        alice_score = dfs(0, len(piles) - 1)
        return alice_score > total - alice_score




            
            








        