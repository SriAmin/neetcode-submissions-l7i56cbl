class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def subsetRecur(i, arr, res, subset):
            if i == len(arr):
                res.append(list(subset))
                return
            
            subset.append(arr[i])
            subsetRecur(i + 1, arr, res, subset)

            subset.pop()
            subsetRecur(i + 1, arr, res, subset)
        
        subset = []
        res = []
        subsetRecur(0, nums, res, subset)

        return res