if __name__ == '__main__':
    n, d, k, c = map(int, input().split())
    sushi_list = [int(input()) for _ in range(n)]
    sushi_seq = sushi_list[:k]
    answer = 0

    for i in range(n):
        sushi_seq.pop(0)
        sushi_seq.append(sushi_list[(i + k) % N])
        result = max(result, len(set(sushi_seq + [c])))
        if result == d:
            break
    print(answer)