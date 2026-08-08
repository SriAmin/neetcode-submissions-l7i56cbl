class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        tmpEnd = intervals[0][1]
        result = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < tmpEnd:
                result += 1
                tmpEnd = min(tmpEnd, intervals[i][1])
            else:
                tmpEnd = intervals[i][1]
        return result