class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        resIdx = 0
        n = len(gas)
        total = 0

        for i in range(0, n):
            total = total + (gas[i] - cost[i])
            if total < 0:
                total = 0
                resIdx = i + 1
        return resIdx
