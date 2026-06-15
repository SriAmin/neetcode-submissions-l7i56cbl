class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(i, arr, res, subset):
            if i == len(arr):
                res.append(list(subset))
                return
            subset.append(arr[i])
            dfs(i + 1, arr, res, subset)

            subset.pop()
            dfs(i + 1, arr, res, subset)
        
        subset = []
        res = []
        dfs(0, nums, res, subset)
        return res