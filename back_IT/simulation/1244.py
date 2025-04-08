def change_switch(x):
    if switch_list[x] == 0:
        switch_list[x] = 1
    else:
        switch_list[x] = 0


if __name__ == '__main__':
    switch = int(input())
    switch_list = [-1] + list(map(int, input().split()))
    student = int(input())

    for _ in range(student):
        gender, num = map(int, input().split())

        if gender == 1:
            for i in range(num, switch + 1, num):
                change_switch(i)
        else:
            change_switch(num)
            for i in range(switch // 2):
                if num - i < 1 or num + i > switch:
                    break
                if switch_list[num - i] == switch_list[num + i]:
                    change_switch(num + i)
                    change_switch(num - i)

    for i in range(1, switch + 1):
        print(switch_list[i], end=" ")
        if i % 20 == 0:
            print()