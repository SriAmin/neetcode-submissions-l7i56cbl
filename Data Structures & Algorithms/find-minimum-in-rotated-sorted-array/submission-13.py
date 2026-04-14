class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:
            mid = (l + r) // 2
            print(l)
            print(r)
            print(mid)
            print("-------")
            if nums[r] > nums[l]:
                res = min(res, nums[l])
                break
            res = min(res, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        return res