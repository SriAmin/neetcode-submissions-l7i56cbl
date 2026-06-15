class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, subset):
            tmpSum = sum(subset)
            if tmpSum == target:
                res.append(subset.copy())
                return
            for j in range(i, len(nums)):
                if tmpSum + nums[j] > target:
                    return
                subset.append(nums[j])
                dfs(j, subset)
                subset.pop()
                
        dfs(0, [])
        return res