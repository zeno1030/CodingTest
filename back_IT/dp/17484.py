if __name__ == '__main__':
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    dp = [[[0, 0, 0] for _ in range(m)]] + [[[float('inf'), float('inf'), float('inf')] for _ in range(m)] for _ in range(n)]
    min_value = float('inf')
    for i in range(1, n + 1):
        for j in range(m):
            if j < m - 1:
                dp[i][j][0] = min(dp[i - 1][j + 1][1], dp[i - 1][j + 1][2]) + matrix[i - 1][j]
            if 0 < j:
                dp[i][j][2] = min(dp[i - 1][j - 1][1], dp[i - 1][j - 1][0]) + matrix[i - 1][j]
            dp[i][j][1] = min(dp[i - 1][j - 1][0], dp[i - 1][j][2]) + matrix[i - 1][j]

        for row in dp[i]:
            for each in row:
                min_value = min(min_value, each)

    print(min_value)
