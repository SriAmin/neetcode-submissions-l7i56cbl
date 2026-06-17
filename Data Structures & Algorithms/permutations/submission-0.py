class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, arr):
            if i == len(nums):
                res.append(arr.copy())
                return
            
            for j in range(i, len(nums)):
                arr[i], arr[j] = arr[j], arr[i]

                dfs(i + 1, arr)

                arr[i], arr[j] = arr[j], arr[i]
        
        dfs(0, nums)
        return res