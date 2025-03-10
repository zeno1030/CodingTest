# n가지 종류의 동전이 있고 가치는 다르다. 적당히 사용해서 k원이 되도록 하고 싶다.
# 사용한 동전의 구성이 같은데, 순서만 다른 것은 같은 경우이다.

if __name__ == '__main__':
    n, k = map(int, input().split())
    coin = []

    for _ in range(n):
        coin.append(int(input()))

