import sys

if __name__ == '__main__':
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))

    left, right = 0, 0
    hap = 0
    min_length = sys.maxsize
    while True:
        if hap >= s:
            min_length = min(min_length, right - left)
            hap -= arr[left]
            left += 1
        elif right == n:
            break
        else:
            hap += arr[right]
            right += 1


    if min_length == sys.maxsize:
        print(0)
    else:
        print(min_length)