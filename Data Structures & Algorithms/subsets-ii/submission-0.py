class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        tmpRes = set()
        def dfs(i, subset):
            if i == len(nums):
                tup = tuple(sorted(subset))
                tmpRes.add(tup)
                return
            subset.append(nums[i])
            dfs(i + 1, subset)

            subset.pop()
            dfs(i+1, subset)

        dfs(0, [])
        res = []
        for pair in tmpRes:
            res.append(list(pair))
        return res