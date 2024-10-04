def calc(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)


if __name__ == "__main__":
    n = int(input())
    building = list(map(int, input().split()))
    answer = 0
    for idx, value in enumerate(building):
        view_max = 0
        left_max = float('inf')
        right_max = -float('inf')

        for i in range(idx + 1, n):
            c = calc(idx + 1, value, i + 1, building[i])
            if c > right_max:
                right_max = c
                view_max += 1

        for i in range(idx - 1, -1, -1):
            c = calc(idx + 1, value, i + 1, building[i])
            if c < left_max:
                left_max = c
                view_max += 1
        answer = max(answer, view_max)
    print(answer)