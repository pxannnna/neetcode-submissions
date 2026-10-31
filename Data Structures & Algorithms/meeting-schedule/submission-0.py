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
        for i in range(len(intervals)-1):
            s1, e1 = intervals[i].start, intervals[i].end
            s2, e2 = intervals[i + 1].start, intervals[i + 1].end
            if s2 < e1:
                return False
        
        return True

