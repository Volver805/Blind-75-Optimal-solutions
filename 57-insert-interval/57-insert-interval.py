class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        s = False
        if not intervals:
            return [newInterval]
        while i < len(intervals):
            if newInterval[0] > intervals[i][1]:
                i += 1
            elif newInterval[1] < intervals[i][0]:
                intervals.insert(i, newInterval)
                return intervals
            else:
                intervals[i][0] = min(newInterval[0], intervals[i][0])
                intervals[i][1] = max(newInterval[1], intervals[i][1])
                j = i+1
                while j < len(intervals) and intervals[i][1] >= intervals[j][0]:
                    intervals[i][0] = min(intervals[j][0], intervals[i][0])
                    intervals[i][1] = max(intervals[j][1], intervals[i][1])
                    del intervals[j]
                return intervals
        intervals.append(newInterval)
        return intervals