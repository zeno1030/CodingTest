if __name__ == '__main__':
    h, w, n, m = map(int, input().split())

    h_answer, w_answer =  h // (n + 1), w // (m + 1)

    if h % (n + 1) != 0:
        h_answer += 1
    if w % (m + 1) != 0:
        w_answer += 1
    print(h_answer * w_answer)
