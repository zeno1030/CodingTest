if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        clothes = int(input())
        clothes_list = set([input() for _ in range(clothes)])

        print(clothes_list)