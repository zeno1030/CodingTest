if __name__ == '__main__':
    arr = input()
    result = []
    size = arr.count('a')
    circle_arr = arr * 2
    for i in range(len(arr)):
        b_count = 0
        for j in range(size):
            index =  i + j
            if circle_arr[index] == 'b':
                b_count += 1
        result.append(b_count)

    print(min(result))


