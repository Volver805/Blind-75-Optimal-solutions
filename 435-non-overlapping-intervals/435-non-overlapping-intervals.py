class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        r = 0
        x = []
        for interval in intervals:
            if not x or x[-1][1] <= interval[0]:
                x.append(interval)
            else:
                if interval[1] < x[-1][1]:
                    x[-1] = interval
                r += 1
        return r
    