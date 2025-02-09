def solution(n, edge):
    answer = 0
    temp = 0
    checked_values = []
    for i in range(len(edge)):
        if edge[i][0] > edge[i][1]:
            temp = edge[i][0]
            edge[i][0] = edge[i][1]
            edge[i][1] = temp
    edge.sort()
    print(edge)
    for pair in edge:
        print(pair[1], answer)
        if pair[0] in checked_values and pair[0] != 1:
            answer += 1
        else:
            checked_values.append(pair[1])
    print(checked_values)



    return answer