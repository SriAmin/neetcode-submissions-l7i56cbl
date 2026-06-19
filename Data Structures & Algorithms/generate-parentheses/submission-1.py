class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(l, r, substr):
            if l >= n and r >= n:
                res.append(substr)
                return
            if l < n:
                dfs(l + 1, r, substr + "(")
            if r < l:
                dfs(l, r + 1, substr + ")")
        dfs(1, 0, "(")
        return res
