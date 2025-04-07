if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        a = int(input())
        x, y = 1, 0
        for i in range(a):
            x, y = y, x + y

        print(x ,y)
        