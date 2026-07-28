class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_min = nums[0]
        current_max = nums[0]

        result = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                current_min, current_max = current_max, current_min
            current_min = min(nums[i], nums[i] * current_min)
            current_max = max(nums[i], nums[i] * current_max)

            result = max(result, current_max)

        return result