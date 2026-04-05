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
                if tmpSum < target or l == i:
                    l += 1
                elif tmpSum > target or r == i:
                    r -= 1
                else:
                    if sorted([nums[i], nums[l], nums[r]]) not in output:
                        output.append(sorted([nums[i], nums[l], nums[r]]))
                    l += 1
        return output
        