P = int(input())

for n in range(P):
    arr = list(map(int, input().split()))
    count = 0
    for i in range(1, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                count += 1
    print(n + 1, count)