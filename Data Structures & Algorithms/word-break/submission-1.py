class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {len(s) : True}

        def dfs(i):
            if i in memo:
                return memo[i]
            
            for word in wordDict:
                w = len(word)
                if ((i + w) <= len(s) and s[i: i + w] == word):
                    if dfs(i + w) or (i + w) == len(s):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
        return dfs(0)