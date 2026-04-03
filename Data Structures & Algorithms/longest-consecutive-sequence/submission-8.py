class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(set(nums))

        output = 1
        tmpOutput = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                tmpOutput = tmpOutput + 1
            else:
                if tmpOutput > output:
                    output = tmpOutput
                tmpOutput = 1
        if tmpOutput > output:
            output = tmpOutput
        return output
        # numberSet = set(nums)
        # output = 0
        # index = 0
        # start = False
        # for i in range(len(numberSet)):
        #     if nums[i] - 1 not in numberSet and start == False:
        #         #Start Building
        #         start = True:
