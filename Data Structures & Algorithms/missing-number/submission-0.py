class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xorr = n
        for i in range(n):
            tmp = i ^ nums[i]
            xorr = xorr ^ tmp
        return xorr