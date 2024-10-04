# 존재한 키워드에서 작성한 키워드가 있으면 remove 없으면 그대로 진행
import sys

if __name__ == "__main__":
    n, m = map(int, input().split())
    keyword = dict()
    for _ in range(n):
        keyword[sys.stdin.readline().rstrip()] = 1
    res = n

    for _ in range(m):
        blog = sys.stdin.readline().rstrip().split(',')

        for word in blog:
            if word in keyword.keys():
                if keyword[word] == 1:
                    res -= 1
                    keyword[word] -= 1
        print(res)