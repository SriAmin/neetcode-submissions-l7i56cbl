class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        cache = {i: -1 for i in range(n)}

        def dfs(house):
            if house >= n:
                return 0
            if cache[house] != -1:
                return cache[house]
            cache[house] = max(nums[house] + dfs(house + 2), dfs(house + 1))
            return cache[house]

        return dfs(0)