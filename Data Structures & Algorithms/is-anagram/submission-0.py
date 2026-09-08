class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts_s = dict()
        counts_t = dict()
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            counts_s[s[i]] = 1 + counts_s.get(s[i],0)
            counts_t[t[i]] = 1 + counts_t.get(t[i],0)
        for c in counts_s: #c is a key and might not exits in a t map
            if counts_s[c] != counts_t.get(c,0):
                return False
        return True