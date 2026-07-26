class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n
        
        def isPalindrom(s: str) -> bool:
            return s == s[::-1]
        
        res = []
        for i in range(n):
            l, r = i, i
            while l >= 0 and r < n:
                if isPalindrom(s[l : r + 1]):
                    res.append((l, r))
                    l -= 1
                    r += 1
                else:
                    break
            l, r = i, i + 1
            while l >= 0 and r < n:
                if isPalindrom(s[l : r + 1]):
                    res.append((l, r))
                    l -= 1
                    r += 1
                else:
                    break
        return len(res)
                

        