if __name__ == '__main__':
    h, w = map(int, input().split())
    height = list(map(int, input().split()))

    left, right = 0, w - 1
    left_max = height[left]
    right_max = height[right]
    volume = 0

    while left < right:
        left_max = max(left_max, height[left])
        right_max = max(right_max, height[right])
        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1

    print(volume)