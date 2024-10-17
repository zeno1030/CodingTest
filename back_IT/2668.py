# 첫째 줄에서 숫자를 적저히 뽑으면, 그 뽑힌 정수들이 이루어진
# 재귀를 이용하여 index = 1 부터 넣으면 -> 3
# 배열에 아랫줄 값이 있으면 break

N = int(input())

adj = [0] * (N + 1)

for i in range(1, N + 1):
    adj[i] = int(input())


def dfs(num):
    if not visited[num]:
        visited[num] = True
        next_num = adj[num]
        tmp_up.add(num)
        tmp_bottom.add(next_num)
        if tmp_up == tmp_bottom:
            ans.extend(list(tmp_bottom))
            return
        dfs(next_num)
    visited[num] = False


ans = []

for i in range(1, N + 1):
    visited = [False] * (N + 1)  # 위에 값 기준으로
    tmp_up = set()
    tmp_bottom = set()

    dfs(i)

ans = list(set(ans))
ans.sort()

print(len(ans))
for a in ans:
    print(a)
