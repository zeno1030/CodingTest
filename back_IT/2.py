def solution(h, w, grid):
    def simulate_light(start_x, start_y, direction):
        path = set()
        x, y = start_x, start_y
        dx, dy = direction

        while 0 <= x < w and 0 <= y < h:
            path.add((x, y))
            if grid[y][x] == '/':
                dx, dy = -dy, -dx

            elif grid[y][x] == '\\':
                dx, dy = dy, dx
            x += dx
            y += dy

        return path

    def get_start_positions():
        starts = []
        for i in range(h):
            starts.append((0, i, (1, 0)))  # 왼쪽에서 시작
            starts.append((w-1, i, (-1, 0)))  # 오른쪽에서 시작
        for i in range(w):
            starts.append((i, 0, (0, 1)))  # 위에서 시작
            starts.append((i, h-1, (0, -1)))  # 아래에서 시작
        return starts

    start_positions = get_start_positions()
    max_count = 0

    for i in range(len(start_positions)):
        for j in range(i+1, len(start_positions)):
            path1 = simulate_light(*start_positions[i])
            path2 = simulate_light(*start_positions[j])
            count = len(path1.union(path2))
            max_count = max(max_count, count)

    return max_count
