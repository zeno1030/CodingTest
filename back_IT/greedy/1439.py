if __name__ == '__main__':
    num = list(input().strip())
    num_dict = {'0': 0, '1': 0}
    main_num = num[0]
    num_dict[main_num] += 1

    for n in num:
        if n != main_num:
            main_num = n
            num_dict[main_num] += 1

    print(min(num_dict.values()))

