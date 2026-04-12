class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        min = r
        while l <= r:
            rate = (l + r) // 2
            total_time = 0
            for p in piles:
                total_time += math.ceil(float(p) / rate)
            if total_time <= h:
                min = rate
                r = rate - 1
            else:
                l = rate + 1
        return min
