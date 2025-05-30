if __name__ == '__main__':
    h, w = map(int, input().split())
    arr = list(map(int, input().split()))

    left, right = 0, w - 1
    left_max = arr[left]
    right_max = arr[right]
    answer = 0

    while left < right:
        left_max = max(left_max, arr[left])
        right_max = max(right_max, arr[right])
        if left_max >= right_max:
            answer += right_max - arr[right]
            right -= 1
        else:
            answer += left_max - arr[left]
            left += 1


    print(answer)

