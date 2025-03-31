if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        n = int(input())
        arr = list(map(int, input().split()))
        answer = 0
        arr.reverse()
        last_num = arr[0]

        for i in range(1, n):
            if arr[i] > last_num:
                last_num = arr[i]
            else:
                answer += last_num - arr[i]

        print(answer)