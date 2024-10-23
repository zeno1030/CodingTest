from collections import deque

if __name__ == "__main__":
    N, K = map(int, input().split())
    arr = deque(list(map(int, input().split())))
    visited = deque([False] * N)
    count = 0

    while True:
        count += 1
        arr.rotate(1)
        visited.rotate(1)

        visited[N - 1] = False

        for i in range(N - 2, -1, -1):
            if visited[i] and not visited[i + 1] and arr[i + 1] > 0:
                visited[i], visited[i + 1] = False, True
                arr[i + 1] -= 1

        visited[N - 1] = False

        if arr[0] > 0:
            visited[0] = True
            arr[0] -= 1
        if arr.count(0) >= K:
            break

    print(count)
