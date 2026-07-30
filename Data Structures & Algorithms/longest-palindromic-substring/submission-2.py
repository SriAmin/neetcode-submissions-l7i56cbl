class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxIdx, maxLen = 0, 1
        n = len(s)
        for i in range(n):
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > maxLen:
                    maxIdx = l
                    maxLen = (r - l + 1)
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > maxLen:
                    maxIdx = l
                    maxLen = (r - l + 1)
                l -= 1
                r += 1

        return s[maxIdx: maxIdx + maxLen]