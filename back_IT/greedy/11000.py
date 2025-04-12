import heapq

from scipy.special.cython_special import log_ndtr

if __name__ == '__main__':
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort(key=lambda x: x[0])
    room = []
    heapq.heappush(room, arr[0][1])

    for i in range(1, n):
        if arr[i][0] < room[0]:
            heapq.heappush(room, arr[i][1])
        else:
            heapq.heappop(room)
            heapq.heappush(room, arr[i][1])

    print(len(room))


