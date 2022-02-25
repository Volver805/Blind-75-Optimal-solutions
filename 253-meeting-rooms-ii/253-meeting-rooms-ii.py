class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = []
        intervals.sort(key=lambda x: x[0])
        for start, end in intervals:
            l = True
            print(rooms)
            for i in range(len(rooms)):
                if rooms[i] <= start:
                    rooms[i] = end
                    l=False
                    break
            if l:
                rooms.append(end)
        return len(rooms)