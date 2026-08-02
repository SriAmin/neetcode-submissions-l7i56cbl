class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {len(s) : True}

        def dfs(i):
            if i in cache:
                return cache[i]
                
            for word in wordDict:
                w = len(word)
                if ((i + w) <= len(s) and s[i: i + w] == word):
                    if dfs(i + w):
                        cache[i] = True
                        return True
            cache[i] = False
            return False
        return dfs(0)