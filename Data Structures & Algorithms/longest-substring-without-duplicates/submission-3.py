class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        l = 0
        r = 1
        chars = set({s[l]})
        maxStr = 0
        while r < len(s):
            maxStr = max(maxStr, len(chars))
            if s[r] in chars:
                print(chars)
                while s[r] in chars:
                    chars.remove(s[l])
                    l = l + 1
            chars.add(s[r])
            r = r + 1
        return max(maxStr, len(chars))