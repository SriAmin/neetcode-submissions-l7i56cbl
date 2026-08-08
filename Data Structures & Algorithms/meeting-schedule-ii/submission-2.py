"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        if n == 0: return 0
        start = []
        end = []
        for i in range(n):
            start.append(intervals[i].start)
            end.append(intervals[i].end)

        start.sort()
        end.sort()

        s, e = 0, 0
        count = 1
        res = 0
        for i in range(n):
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            res = max(count, res)
        return res - 1