# 머리의 위치를 찾는다
# 머리 위치의 y값 + 1이 심장위치
# 왼쪽으로 쭉 왼팔 오른쪽으로 쭉 오른팔
# 아래로 쭉 허리
# 허리의 마지막 위치 에서  x 값 -1 y 값 + 1 왼쪽 다리
# 허리의 마지막 위치 에서 x 값 +1 y 값 + 1 오른쪽 다리
def find_heart(x, y):
    h_x, h_y = x + 1, y
    return h_x, h_y


def find_left_hand(x, y):
    global answer
    count = 0
    for i in range(y):
        if arr[x][i] == '*':
            count += 1
    answer.append(count)


def find_right_hand(x, y):
    global answer
    count = 0
    for i in range(y + 1, n):
        if arr[x][i] == '*':
            count += 1
    answer.append(count)


def find_middle(x, y):
    global answer
    count = 0
    for i in range(x + 1, n):
        if arr[i][y] == '*':
            count += 1
        elif arr[i][y] == '_':
            m_x, m_y = i - 1, y
            answer.append(count)
            return m_x, m_y


def find_left_leg(x, y):
    global answer
    count = 0
    l_x, l_y = x + 1, y - 1
    for i in range(l_x, n):
        if arr[i][l_y] == '*':
            count += 1
    answer.append(count)


def find_right_leg(x, y):
    global answer
    count = 0
    r_x, r_y = x + 1, y + 1
    for i in range(r_x, n):
        if arr[i][r_y] == '*':
            count += 1
    answer.append(count)


if __name__ == "__main__":
    n = int(input())
    arr = []
    answer = []
    for _ in range(n):
        row = input()
        arr.append(list(row))

    found = False

    for i in range(n):
        if found:
            break
        for j in range(n):
            if arr[i][j] == '*':
                h_x, h_y = find_heart(i, j)
                found = True
                break

    find_left_hand(h_x, h_y)
    find_right_hand(h_x, h_y)
    m_x, m_y = find_middle(h_x, h_y)
    find_left_leg(m_x, m_y)
    find_right_leg(m_x, m_y)
    print(h_x + 1, h_y + 1)
    print(*answer)