if __name__ == "__main__":
    n = int(input())
    dp = [1 for _ in range(n)]
    a = list(map(int, input().split()))

    for i in range(n):
        for j in range(i):
            if a[i] > a[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(max(dp))