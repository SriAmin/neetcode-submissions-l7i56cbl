class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, subset):
            if i == len(nums):
                res.append(subset.copy())
                return
            for j in range(i, len(nums)):
                subset[j], subset[i] = subset[i], subset[j]
                dfs(i + 1, subset)
                subset[j], subset[i] = subset[i], subset[j]
        dfs(0, nums)
        return res