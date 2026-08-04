"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        n = len(intervals)

        m1, m2 = 0, 1
        while m1 < m2 and m2 < n:
            s1, e1 = intervals[m1].start, intervals[m1].end
            s2, e2 = intervals[m2].start, intervals[m2].end

            if s1 < e2 and s2 < e1:
                return False
            m1 += 1
            m2 += 1
        return True