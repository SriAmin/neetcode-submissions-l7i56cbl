class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        n = len(nums)
        cache = [[-1] * (target + 1) for _ in range(n + 1)]

        def dfs(i, curSum):
            if curSum == 0:
                return True
            if i >= n or curSum < 0:
                return False
            if cache[i][curSum] != -1:
                return cache[i][curSum]
            
            cache[i][curSum] = (dfs(i + 1, curSum) or dfs(i + 1, curSum - nums[i]))
            return cache[i][curSum]
        return dfs(0, target)
        

        