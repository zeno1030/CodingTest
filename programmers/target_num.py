def solution(numbers, target):
    answer = 0
    results = [0]

    for num in numbers:
        temp = []

        for result in results:
            temp.append(result + num)
            temp.append(result - num)

        results = temp

    for result in results:
        if result == target:
            answer += 1
    return answer