if __name__ == '__main__':
    n = int(input())
    plus = []
    minus = []
    answer = 0
    for _ in range(n):
        num = int(input())
        if num > 1:
            plus.append(num)
        elif num <= 0:
            minus.append(num)
        else:
            answer +=  num

    plus.sort(reverse=True)
    minus.sort()

    for i in range(0, len(plus), 2):
        if i + 1 >= len(plus):
            answer += plus[i]
        else:
            answer += plus[i] * plus[i + 1]

    for i in range(0, len(minus), 2):
        if i + 1 >= len(minus):
            answer += minus[i]
        else:
            answer += minus[i] * minus[i + 1]

    print(answer)