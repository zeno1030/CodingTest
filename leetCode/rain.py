class Solution:
    def trap(height: list[int]) -> int:
        if not height:
            return 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        volumn = 0

        while left < right:
            left_max = max(height[left], left_max)
            right_max = max(height[right], right_max)

            if left_max <= right_max:
                volumn += left_max - height[right]
                left += 1
            else:
                volumn += right_max - height[left]
                right -= 1
        return volumn

    trap([0,1,0,2,1,0,1,3,2,1,2,1])
