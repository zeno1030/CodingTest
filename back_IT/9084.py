def count_ways(coins, M):
    # DP 배열 초기화
    dp = [0] * (M + 1)
    dp[0] = 1  # 0원을 만드는 방법은 1가지 (아무것도 사용하지 않음)

    # 각 동전에 대해 DP 배열 업데이트
    for coin in coins:
        for j in range(coin, M + 1):
            dp[j] += dp[j - coin]

    return dp[M]

# 입력 받기
T = int(input())  # 테스트 케이스 수
for _ in range(T):
    N = int(input())  # 동전 종류 수
    coins = list(map(int, input().split()))  # 동전 종류 입력
    M = int(input())  # 목표 금액 입력

    # 가능한 방법의 수 출력
    print(count_ways(coins, M))
