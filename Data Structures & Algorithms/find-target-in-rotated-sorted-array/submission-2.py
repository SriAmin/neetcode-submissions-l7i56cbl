class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            lNum = nums[l]
            rNum = nums[r]
            midNum = nums[mid]
            if midNum == target:
                return mid
            
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
                    
            # if lNum < target and mid < target or lNum > target or rNum < target:
            #     l = mid + 1
            # elif rNum > target and mid > target or rNum < target or lNum > target:
            #     r = mid - 1
        return -1