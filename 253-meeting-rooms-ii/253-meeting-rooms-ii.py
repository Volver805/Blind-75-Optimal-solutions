class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        h = [intervals[0][1]] # heap contains the end of rooms
        for interval in intervals[1:]:
            # Compare the end of the least waiting room with the current interval start
            if interval[0] >= h[0]:
                heapq.heappop(h)
            heapq.heappush(h, interval[1])
        return len(h)
            