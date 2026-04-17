class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        maxF = 0
        l = 0
        out = 0

        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            maxF = max(maxF, freq[s[r]])
            while (r - l + 1) - maxF > k:
                freq[s[l]] = freq[s[l]] - 1
                l = l + 1
            out = max(out, r - l + 1)
        return out