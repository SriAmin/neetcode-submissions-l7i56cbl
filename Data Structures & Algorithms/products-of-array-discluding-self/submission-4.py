class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arrs = []

        for i in range(len(nums)):
            leftLimit = max(i, 0)
            rightLimit = min(i + 1, len(nums))
            arrs.append(nums[0 : leftLimit] + nums[rightLimit : len(nums)])

        output = []
        for arr in arrs:
            result = 1
            for num in arr:
                result *= num
            output.append(result)
        return output