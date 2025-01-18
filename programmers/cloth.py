from collections import defaultdict


def solution(clothes):
    answer = 1
    clothesDict = defaultdict(list)

    for cloth in clothes:
        clothesDict[cloth[1]].append(cloth[0])

    for _, value in clothesDict.items():
        answer *= (len(value) + 1)

    print(clothesDict)
    return answer - 1