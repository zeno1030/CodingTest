# 가장 왼쪽의 계란을 든다.
# 손에 들고 있는 계란으로 깨지지 않은 다른 계란 중에서 하나를 친다. 단, 손에 든 계란이 깨졌거나 깨지지 않은 다른 계란이 없으면 치지 않고 넘어간다. 이후 손에 든 계란을 원래 자리에 내려놓고 3번 과정을 진행한다.
# 가장 최근에 든 계란의 한 칸 오른쪽 계란을 손에 들고 2번 과정을 다시 진행한다. 단, 가장 최근에 든 계란이 가장 오른쪽에 위치한 계란일 경우 계란을 치는 과정을 종료한다.

def check(eggs):
    count = 0
    for egg in eggs:
        if egg[0] <= 0:
            count += 1

    return count


def dfs(x, eggs):
    global answer

    if x == n:
        answer = max(answer, check(eggs))
        return
    if eggs[x][0] <= 0:
        dfs(x + 1, eggs)
    else:
        is_all_broken = True
        for i in range(n):
            if x != i and eggs[i][0] > 0:
                is_all_broken = False
                eggs[x][0] -= eggs[i][1]
                eggs[i][0] -= eggs[x][1]
                dfs(x + 1, eggs)
                eggs[x][0] += eggs[i][1]
                eggs[i][0] += eggs[x][1]
        if is_all_broken:
            dfs(n, eggs)

if __name__ == '__main__':
    n = int(input())
    eggs = []
    answer = 0
    for _ in range(n):
        s, w = map(int, input().split())
        eggs.append([s, w])

    dfs(0, eggs)
    print(answer)