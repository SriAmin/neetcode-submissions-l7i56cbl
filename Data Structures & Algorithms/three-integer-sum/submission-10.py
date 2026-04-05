class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        output = []
        for i in range(len(nums) - 2):
            target = -nums[i]
            l = i + 1
            r = len(nums) - 1

            while l < r:
                tmpSum = nums[l] + nums[r]
                if tmpSum < target:
                    l += 1
                elif tmpSum > target:
                    r -= 1
                else:
                    if [nums[i], nums[l], nums[r]] not in output:
                        output.append([nums[i], nums[l], nums[r]])
                    l += 1
        return output
        