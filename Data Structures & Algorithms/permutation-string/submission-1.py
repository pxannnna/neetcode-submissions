class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = {}
        for ch in s1:
            need[ch] = need.get(ch, 0) + 1

        window = {}
        l = 0
        for r in range(len(s2)):
            ch = s2[r]
            window[ch] = window.get(ch, 0) + 1

            # keep window size == len(s1)
            if r - l + 1 > len(s1):
                left_ch = s2[l]
                window[left_ch] -= 1
                if window[left_ch] == 0:
                    del window[left_ch]
                l += 1

            if window == need:
                return True

        return False

