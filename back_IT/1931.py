if __name__ == "__main__":
    n = int(input())

    time = []
    for i in range(n):
        s_t, e_t = map(int, input().split())
        time.append((s_t, e_t))
    time.sort(key=lambda x: (x[1], x[0]))
    last = 0
    count = 0
    for i, j in time:
        if i >= last:
            count += 1
            last = j
    print(count)