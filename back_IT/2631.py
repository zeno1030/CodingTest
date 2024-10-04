if __name__ == "__main__":
    n = int(input())
    children = []
    answer = 0
    for _ in range(n):
        children.append(int(input()))
    dp = [1 for _ in range(n)]

    for i in range(n):
        for j in range(i):
            if children[i] > children[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(n - max(dp))