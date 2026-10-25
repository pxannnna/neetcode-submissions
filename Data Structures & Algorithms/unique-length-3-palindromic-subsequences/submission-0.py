class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        #left = set
        #right = hashmap becasue we are poping the middle


        res= set()
        left = set()
        right = collections.Counter(s) # count acccurences of every character
        for i in range(len(s)):
            right[s[i]] -= 1
            if right[s[i]] == 0:
                right.pop(s[i])
            for j in range(26):
                c= chr(ord('a') + j)
                if c in left and c in right:
                    res.add((s[i], c)) #makes sure we dont count duplicates
            left.add(s[i])
        
        return len(res)

        