n,d,k,c = map(int, input().split())
plate = []
for i in range(n):
    plate.append(int(input()))

max_sushi = 0

#방법1 (시간초과 실패)
for i in range(n):
    tmp = set()
    tmp.add(c)
    for j in range(k):
        tmp.add(plate[i-n+j])
    #print(tmp , end=' ')
    max_sushi = max(max_sushi, len(tmp))