from collections import deque


def is_available(x):
    l = [i for i in x]
    q = deque()
    q.append(l[0])
    l.remove(l[0])

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (nx, ny) in l:
                q.append((nx, ny))
                l.remove((nx, ny))

        if len(l) == 0:
            return True
        return False


def dfs(depth):
    global answer

    if len(s) == 7:
        # 다솜이가 4개 이상, 인접해있으면 answer ++, 리턴
        if n.count('S') >= 4 and is_available(s):
            answer += 1
        return
    for i in (depth, 25):
        x, y = idx[i]
        s.append((x, y))
        n.append(board[x][y])
        dfs(depth + 1)
        s.pop()
        n.pop()


if __name__ == '__main__':
    board = [list(input()) for _ in range(5)]
    idx = [(i, j) for i in range(5) for j in range(5)]
    s = []
    n = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    answer = 0
    # dfs를 통해 7명 구성원 다솜이 판단
    dfs(0)