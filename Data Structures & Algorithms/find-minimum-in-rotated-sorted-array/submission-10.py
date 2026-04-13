class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l = 0
        r = len(nums)-1
        output = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                output = min(output, nums[l])
                break
            mid = (l + r) // 2
            output = min(output, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return output