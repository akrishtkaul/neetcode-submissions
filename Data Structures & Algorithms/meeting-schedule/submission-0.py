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

        for i in range(len(meetings)):
            for j in range(i+1, len(meetings)):
                print (meetings[i].end , meetings[j].start)
                if meetings[i].end > meetings[j].start:
                    return False

        print(meetings)
        return True



