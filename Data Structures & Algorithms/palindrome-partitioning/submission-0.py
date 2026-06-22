class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def isPalindrom(w):
            return w == w[::-1]
        def dfs(i, sub):
            n = len(s)
            if i >= n:
                res.append(sub.copy())
                return

            for j in range(i, n):
                w = s[i:j+1]
                if isPalindrom(w):
                    dfs(j + 1, sub + [w])
        dfs(0, [])
        return res