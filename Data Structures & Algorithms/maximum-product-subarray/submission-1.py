class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        current_min, current_max = 1, 1

        for num in nums:
            tmp = current_max * num
            current_max = max(num, num * current_max, num * current_min)
            current_min = min(num, tmp, current_min * num)
            res = max(res, current_max)
        return res
