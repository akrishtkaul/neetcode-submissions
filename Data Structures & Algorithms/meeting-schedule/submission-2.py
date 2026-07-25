"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        meetings = sorted(intervals, key = lambda meeting: meeting.start)

        for i in range(1, len(meetings)):
            if meetings[i-1].end > meetings[i].start:
                return False

        return True



