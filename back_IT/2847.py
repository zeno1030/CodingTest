def solution(levels):
    decrease = 0
    for i in range(len(levels) - 2, -1, -1):
        if levels[i] >= levels[i + 1]:
            diff = levels[i] - levels[i + 1] + 1
            levels[i] -= diff
            decrease += diff
    return decrease

if __name__ == "__main__":
    n = int(input())
    levels = [int(input()) for _ in range(n)]
    print(solution(levels))