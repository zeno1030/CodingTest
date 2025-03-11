# n가지 종류의 동전이 있고 가치는 다르다. 적당히 사용해서 k원이 되도록 하고 싶다.
# 사용한 동전의 구성이 같은데, 순서만 다른 것은 같은 경우이다.

if __name__ == '__main__':
    n, k = map(int, input().split())

    coins = []
    for i in range(n):
        coins.append(int(input()))
    coins.sort()

    DP = [0] * (k + 1)
    DP[0] = 1
    for c in coins:
        for i in range(c, k + 1):
            DP[i] += DP[i - c]
    print(DP[k])

