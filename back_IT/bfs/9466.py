def bfs(x):
    global visited
    if x == arr[x]:
        answer.add(x)
        visited = []
        return
    if x in visited:
        for num in visited:
            answer.add(num)
        visited = []
        return

    visited.append(x)
    bfs(arr[x])


if __name__ == '__main__':
    T = int(input())
    answer = set()
    visited = []
    for _ in range(T):
        n = int(input())
        arr = [0] + list(map(int, input().split()))

        for i in range(1, n + 1):
            bfs(i)

        print(n - len(answer))

