if __name__ == '__main__':
    n = int(input())
    pillars = [tuple(map(int, input().split())) for _ in range(n)]

    # x 좌표 기준으로 정렬
    pillars.sort()

    left, right = 0, n - 1
    left_max = pillars[left][1]
    right_max = pillars[right][1]
    max_height = max(pillars, key=lambda x: x[1])  # 가장 높은 기둥 찾기
    max_idx = pillars.index(max_height)  # 최고 기둥 인덱스

    area = 0
    prev_x = pillars[left][0]

    # 왼쪽 -> 최고점까지
    while left < max_idx:
        if pillars[left][1] > left_max:
            left_max = pillars[left][1]
        area += (pillars[left + 1][0] - prev_x) * left_max
        prev_x = pillars[left + 1][0]
        left += 1

    # 오른쪽 -> 최고점까지
    prev_x = pillars[right][0]
    while right > max_idx:
        if pillars[right][1] > right_max:
            right_max = pillars[right][1]
        area += (prev_x - pillars[right - 1][0]) * right_max
        prev_x = pillars[right - 1][0]
        right -= 1

    # 최고점 기둥 추가
    area += max_height[1]

    print(area)
