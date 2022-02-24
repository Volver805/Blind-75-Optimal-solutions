we wnat to sort the intervals (logN) first. **Now to know if two elements are overlapping or not we just need to check if the first elements end is bigger or equal to the second element start, if Yes there's an overlap if not these to intervals don't overlap**
create a list to sort the result
iterate on every intervals and compare it to the last element of our result list
- If there is no overlap add it to our result list (or if the result list is empty)
- If there's an overlap set the end of the last element in the result list to the maximum between the end of it and this interval (we don't have to worry about the start as the intervals are sorted)
