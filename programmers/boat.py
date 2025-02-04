def solution(people, limit):
    answer = 0
    people.sort()
    left, right = 0, len(people) - 1

    while left < right:
        if people[left] + people[right] <= limit:
            answer += 1
            left += 1
        right -= 1

    return len(people) - answer