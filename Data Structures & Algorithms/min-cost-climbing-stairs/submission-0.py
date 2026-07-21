class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cache = [-1] * n

        def dfs(stair):
            if stair >= n:
                return 0
            if cache[stair] != -1:
                return cache[stair]
            cache[stair] = cost[stair] + min(dfs(stair + 1), dfs(stair + 2))
            return cache[stair]

        return min(dfs(0), dfs(1))