class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []
        def isPalindrom(w):
            return w == w[::-1]
        
        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if isPalindrom(s[i:j+1]):
                    part.append(s[i: j + 1])
                    dfs(j + 1)
                    part.pop()
        dfs(0)
        return res