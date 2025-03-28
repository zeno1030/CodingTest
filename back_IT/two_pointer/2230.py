import sys

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    num = [int(sys.stdin.readline()) for _ in range(n)]
    min_num = sys.maxsize

    left, right = 0, 0
    num.sort()
    while right < n:
        diff = num[right] - num[left]
        if diff < m:
            right += 1
        elif diff > m:
            min_num = min(min_num, diff)
            left += 1
        else:
            min_num = m

    print(min_num)

