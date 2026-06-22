class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []
        def isPalindrom(w):
            return w == w[::-1]
        def dfs(i):
            n = len(s)
            if i >= n:
                res.append(part.copy())
                return

            for j in range(i, n):
                w = s[i:j+1]
                if isPalindrom(w):
                    part.append(w)
                    dfs(j + 1)
                    part.pop()
        dfs(0)
        return res