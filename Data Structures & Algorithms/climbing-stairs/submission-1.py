class Solution:
    def climbStairs(self, n: int) -> int: 
        cache = [-1] * n

        def dfs(num):
            if num > n:
                return 0
            if num == n:
                return 1
            if cache[num] != -1:
                return cache[num]
            
            cache[num] = dfs(num+1) + dfs(num+2)
            return cache[num]
            
        return dfs(0)