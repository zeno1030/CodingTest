def find_areas(M, N, K, rectangles):
    grid = [[0] * N for _ in range(M)]

    # 직사각형 표시
    for x1, y1, x2, y2 in rectangles:
        for i in range(y1, y2):
            for j in range(x1, x2):
                grid[i][j] = 1  # 직사각형 부분을 1로 표시

    # 영역 탐색을 위해 BFS 또는 DFS 사용
    def bfs(start):
        queue = [start]
        area_size = 0
        while queue:
            x, y = queue.pop(0)
            if 0 <= x < M and 0 <= y < N and grid[x][y] == 0:
                grid[x][y] = 1  # 방문 표시
                area_size += 1
                # 인접한 위치 탐색
                queue.append((x + 1, y))
                queue.append((x - 1, y))
                queue.append((x, y + 1))
                queue.append((x, y - 1))
        return area_size

    areas = []

    # 모든 위치를 탐색하여 영역 계산
    for i in range(M):
        for j in range(N):
            if grid[i][j] == 0:  # 방문하지 않은 지역
                area_size = bfs((i, j))
                if area_size > 0:
                    areas.append(area_size)

    return sorted(areas)


# 입력 예시
M, N, K = map(int, input().split())
rectangles = []
for _ in range(K):
    a, b, c, d = map(int, input().split())
    rectangles.append((a, b, c, d))


# 영역 계산
result = find_areas(M, N, K, rectangles)

# 결과 출력
print(len(result))
print(" ".join(map(str, result)))
