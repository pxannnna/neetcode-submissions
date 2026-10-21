class Solution:
    def compress(self, chars: List[str]) -> int:
        result, i, count = "", 0, 1

        while i < len(chars):
            if i + 1 < len(chars) and chars[i] == chars[i+1]:
                count += 1
            else:
                if count > 1:
                    result += chars[i] + str(count)
                else:
                    result += chars[i]
                count = 1
            i += 1

        chars[:len(chars)] = result
        return len(result)