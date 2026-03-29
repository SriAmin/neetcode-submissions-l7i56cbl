class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in numDict:
                return [numDict[diff], i]
            numDict[nums[i]] = i
        return [0, 0]