class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        """
        Intuition:
            Since we're minimizing number of intervals to remove,
            it seems like we should try to remove longer running
            intervals.
            
            All things considered, longer running intervals should
            end later, right? So what if we take the intervals
            which end earliest first!
        """
        
        # sort intervals by finish time, ascending
        intervals.sort(key=lambda x: x[1])
        
        # greedy strategy:
        # accept every interval that isn't conflicting
        # add up removals
        end_so_far = intervals[0][1]
        removed = 0
        
        for start, finish in intervals[1:]:
            if start < end_so_far:
                removed += 1
            else:
                end_so_far = finish
            
        return removed