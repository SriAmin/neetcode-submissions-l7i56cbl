class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        cache = [[-1] * 2 for _ in range(n)]

        def dfs(house, flag):
            if house >= n or (flag and house == n -1):
                return 0
            if cache[house][flag] != -1:
                return cache[house][flag]
            
            cache[house][flag] = max(nums[house] + dfs(house + 2, flag or (house == 0)), dfs(house + 1, flag))
            return cache[house][flag]

        return max(dfs(0, False), dfs(1, True)) 
