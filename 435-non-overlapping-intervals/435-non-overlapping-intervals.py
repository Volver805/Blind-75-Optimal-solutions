class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Greedy by End
        if not intervals:
            return
        intervals.sort(key=lambda x: x[1])
        lastEnd = intervals[0][1]
        r = 0
        for start, end in intervals[1:]:
            if start < lastEnd:
                r += 1
            else:
                lastEnd = end
        return r
                