class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()

        def dfs(i, s):
            if s == target:
                res.append(subset.copy())
                return
            if s > target or i == len(candidates):
                return

            subset.append(candidates[i])
            dfs(i + 1, s + candidates[i])
            subset.pop()

            j = i + 1
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            dfs(j, s)
        dfs(0, 0)
        return res