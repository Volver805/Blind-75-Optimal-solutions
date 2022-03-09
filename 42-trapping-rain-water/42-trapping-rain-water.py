class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_left, max_right = height[left], height[right]
        res = 0
        while left < right:
            max_left, max_right = max(max_left, height[left]), max(max_right, height[right])
            if max_right < max_left:
                res += max_right - height[right]
                right -= 1
            else:
                res += max_left - height[left]
                left += 1
        return res